import os
import pandas as pd
import mysql.connector


# ============================================================
# MySQL Configuration
# ============================================================

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    
    "user": "D2_92672Pranay",
    "password": "manager",
    "database": "vehicle_legacy"
}


# ============================================================
# Output directory
# ============================================================

OUTPUT_DIR = "migration/output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# Connect to MySQL
# ============================================================

connection = mysql.connector.connect(**DB_CONFIG)

print("Connected to MySQL successfully.")


# ============================================================
# Tables to extract
# ============================================================

tables = [
    "manufacturers",
    "dealers",
    "customers",
    "vehicles",
    "payments"
]


# ============================================================
# Extract each table
# ============================================================

for table in tables:

    print(f"\nExtracting {table}...")

    query = f"SELECT * FROM {table}"

    df = pd.read_sql(query, connection)

    output_file = os.path.join(
        OUTPUT_DIR,
        f"{table}.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Created {output_file} "
        f"({len(df):,} records)"
    )


# ============================================================
# Close connection
# ============================================================

connection.close()

print("\nMySQL connection closed.")
print("CSV extraction completed successfully.")