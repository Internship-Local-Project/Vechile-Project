import os
import logging
import functions_framework

from google.cloud import bigquery
from google.cloud import storage

from config import (
    PROJECT_ID,
    DATASET_ID,
    BUCKET_NAME,
    FILE_CONFIG,
)

from utils import (
    load_schema,
    validate_csv,
    validate_or_apply_table_schema,
    generate_job_id,
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


bq_client = bigquery.Client(project=PROJECT_ID)
storage_client = storage.Client(project=PROJECT_ID)


@functions_framework.cloud_event
def gcs_to_bigquery(cloud_event):

    data = cloud_event.data

    bucket_name = data.get("bucket")
    file_name = data.get("name")
    generation = str(data.get("generation", ""))

    # -----------------------------
    # Event validation
    # -----------------------------

    if not bucket_name or not file_name or not generation:
        raise ValueError("Invalid GCS event.")

    if bucket_name != BUCKET_NAME:
        raise ValueError(f"Unexpected bucket: {bucket_name}")

    # Ignore folders
    if file_name.endswith("/"):
        return

    base_file_name = os.path.basename(file_name)

    # Ignore non CSV
    if not base_file_name.lower().endswith(".csv"):
        logger.info("Ignoring non CSV file: %s", base_file_name)
        return

    # -----------------------------
    # Check supported file
    # -----------------------------

    file_config = FILE_CONFIG.get(base_file_name)

    if not file_config:
        raise ValueError(
            f"Unsupported CSV file: {base_file_name}"
        )

    table_name = file_config["table"]
    schema_path = file_config["schema"]

    # -----------------------------
    # Load external schema
    # -----------------------------

    schema = load_schema(schema_path)

    # -----------------------------
    # Get exact GCS object
    # -----------------------------

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(
        file_name,
        generation=int(generation)
    )

    blob.reload()

    # -----------------------------
    # Validate CSV
    # -----------------------------

    validate_csv(
        blob,
        schema
    )

    # -----------------------------
    # BigQuery destination
    # -----------------------------

    table_id = (
        f"{PROJECT_ID}."
        f"{DATASET_ID}."
        f"{table_name}"
    )

    # Apply schema if table has none.
    # Otherwise validate schema.
    validate_or_apply_table_schema(
        bq_client,
        table_id,
        schema
    )

    # -----------------------------
    # BigQuery load configuration
    # -----------------------------

    job_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=False,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        max_bad_records=0,
        ignore_unknown_values=False,
        allow_quoted_newlines=True,
    )

    gcs_uri = f"gs://{bucket_name}/{file_name}"

    # Prevent duplicate event loading
    job_id = generate_job_id(
        bucket_name,
        file_name,
        generation
    )

    logger.info(
        "Loading %s -> %s",
        gcs_uri,
        table_id
    )

    try:

        load_job = bq_client.load_table_from_uri(
            gcs_uri,
            table_id,
            job_id=job_id,
            job_config=job_config
        )

        load_job.result()

    except Exception as error:

        # If same job already completed because
        # Eventarc delivered duplicate event
        try:
            existing_job = bq_client.get_job(job_id)
            existing_job.result()

            logger.info(
                "File already processed: %s",
                base_file_name
            )

            return

        except Exception:
            raise error

    logger.info(
        "Successfully loaded %s into %s",
        base_file_name,
        table_id
    )