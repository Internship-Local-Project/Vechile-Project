gcloud functions deploy gcs_to_bigquery `
    --gen2 `
    --runtime=python312 `
    --region=asia-south1 `
    --source="C:\Users\Sudarshan\OneDrive\Desktop\proj\Vechile-ETL-Project\cloud_function\gcs_to_bronze_layer" `
    --entry-point=gcs_to_bigquery `
    --trigger-bucket=vehicle-etl-migration-2026-12345 `
    --service-account="vehicle-etl-sa@vechile-etl-migration.iam.gserviceaccount.com"