PROJECT_ID = "vechile-etl-migration"
DATASET_ID = "bronze"
BUCKET_NAME = "vehicle-etl-migration-2026-12345"

FILE_CONFIG = {
    "customers.csv": {
        "table": "bronze_customers",
        "schema": "schemas/customers.json"
    },
    "dealers.csv": {
        "table": "bronze_dealers",
        "schema": "schemas/dealers.json"
    },
    "manufacturers.csv": {
        "table": "bronze_manufacturers",
        "schema": "schemas/manufacturers.json"
    },
    "payments.csv": {
        "table": "bronze_payments",
        "schema": "schemas/payments.json"
    },
    "vehicles.csv": {
        "table": "bronze_vehicles",
        "schema": "schemas/vehicles.json"
    }
}