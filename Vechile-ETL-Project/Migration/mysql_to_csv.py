import os
import pandas as pd
import mysql.connector



DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    
    "user": "D2_92672Pranay",
    "password": "manager",
    "database": "vehicle_legacy"
}




OUTPUT_DIR = "migration/output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


connection = mysql.connector.connect(**DB_CONFIG)

print("Connected to MySQL successfully.")




tables = [
    "manufacturers",
    "dealers",
    "customers",
    "vehicles",
    "payments"
]




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



connection.close()

print("\nMySQL connection closed.")
print("CSV extraction completed successfully.")