import csv
import hashlib
import json
import os

from google.cloud import bigquery
from google.api_core.exceptions import NotFound


def load_schema(schema_relative_path):

    base_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    schema_path = os.path.join(
        base_dir,
        schema_relative_path
    )

    if not os.path.exists(schema_path):
        raise FileNotFoundError(
            f"Schema not found: {schema_path}"
        )

    with open(
        schema_path,
        "r",
        encoding="utf-8"
    ) as file:

        schema_json = json.load(file)

    if not schema_json:
        raise ValueError(
            f"Schema is empty: {schema_relative_path}"
        )

    fields = []

    for field in schema_json:

        fields.append(
            bigquery.SchemaField(
                field["name"],
                field["type"],
                mode=field.get(
                    "mode",
                    "NULLABLE"
                )
            )
        )

    return fields


def validate_csv(blob, schema):

    # -----------------------------
    # File size
    # -----------------------------

    if not blob.size or blob.size == 0:
        raise ValueError(
            f"Empty CSV file: {blob.name}"
        )

    expected_header = [
        field.name
        for field in schema
    ]

    # -----------------------------
    # Read header
    # -----------------------------

    with blob.open(
        "rt",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.reader(file)

        actual_header = next(
            reader,
            None
        )

        if not actual_header:
            raise ValueError(
                f"CSV has no header: {blob.name}"
            )

        actual_header = [
            column.strip()
            for column in actual_header
        ]

        # -----------------------------
        # Duplicate header columns
        # -----------------------------

        if len(actual_header) != len(
            set(actual_header)
        ):
            raise ValueError(
                f"Duplicate columns found: "
                f"{actual_header}"
            )

        # -----------------------------
        # Header/schema validation
        # -----------------------------

        if actual_header != expected_header:

            missing = [
                col
                for col in expected_header
                if col not in actual_header
            ]

            extra = [
                col
                for col in actual_header
                if col not in expected_header
            ]

            raise ValueError(
                f"CSV header mismatch. "
                f"Missing={missing}, "
                f"Extra={extra}"
            )

        # -----------------------------
        # Check at least one row exists
        # -----------------------------

        first_row = next(
            reader,
            None
        )

        if first_row is None:
            raise ValueError(
                f"CSV contains header only: "
                f"{blob.name}"
            )


def validate_or_apply_table_schema(
    client,
    table_id,
    expected_schema
):

    try:
        table = client.get_table(
            table_id
        )

    except NotFound:
        raise ValueError(
            f"BigQuery table not found: "
            f"{table_id}"
        )

    # -----------------------------
    # Empty table schema
    # -----------------------------

    if not table.schema:

        table.schema = expected_schema

        client.update_table(
            table,
            ["schema"]
        )

        return

    # -----------------------------
    # Existing schema validation
    # -----------------------------

    existing = [
        (
            field.name,
            field.field_type,
            field.mode
        )
        for field in table.schema
    ]

    expected = [
        (
            field.name,
            field.field_type,
            field.mode
        )
        for field in expected_schema
    ]

    if existing != expected:

        raise ValueError(
            f"BigQuery schema mismatch "
            f"for {table_id}"
        )


def generate_job_id(
    bucket,
    file_name,
    generation
):

    identifier = (
        f"{bucket}:"
        f"{file_name}:"
        f"{generation}"
    )

    hash_value = hashlib.sha256(
        identifier.encode("utf-8")
    ).hexdigest()[:32]

    return f"bronze_load_{hash_value}"