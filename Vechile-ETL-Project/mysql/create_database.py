import mysql.connector


# --------------------------------------------------
# MySQL connection
# --------------------------------------------------

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="MyNewPassword@123"
)


cursor = connection.cursor()


# --------------------------------------------------
# Create database
# --------------------------------------------------

cursor.execute("""
    CREATE DATABASE IF NOT EXISTS vehicle_legacy
""")

cursor.execute("""
    USE vehicle_legacy
""")


# --------------------------------------------------
# 1. Manufacturers
# --------------------------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS manufacturers (
        manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
        manufacturer_name VARCHAR(100) NOT NULL,
        country VARCHAR(100),
        founded_year SMALLINT,
        headquarters VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")


# --------------------------------------------------
# 2. Dealers
# --------------------------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS dealers (
        dealer_id INT AUTO_INCREMENT PRIMARY KEY,
        dealer_name VARCHAR(150) NOT NULL,
        city VARCHAR(100) NOT NULL,
        state VARCHAR(100),
        address VARCHAR(255),
        phone VARCHAR(20),
        email VARCHAR(150),
        dealer_type VARCHAR(50),
        opening_date DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")


# --------------------------------------------------
# 3. Customers
# --------------------------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(150),
        phone VARCHAR(20),
        date_of_birth DATE,
        city VARCHAR(100),
        state VARCHAR(100),
        registration_date DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")


# --------------------------------------------------
# 4. Vehicles
# --------------------------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        vehicle_id INT AUTO_INCREMENT PRIMARY KEY,

        manufacturer_id INT NOT NULL,
        dealer_id INT NOT NULL,
        customer_id INT NULL,

        vin VARCHAR(50) NOT NULL UNIQUE,
        model_name VARCHAR(100) NOT NULL,
        vehicle_type VARCHAR(50),
        fuel_type VARCHAR(50),
        transmission VARCHAR(50),
        manufacturing_year YEAR,
        color VARCHAR(50),

        price DECIMAL(12,2) NOT NULL,

        sale_date DATE NULL,

        vehicle_status VARCHAR(30)
            NOT NULL DEFAULT 'AVAILABLE',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT fk_vehicle_manufacturer
            FOREIGN KEY (manufacturer_id)
            REFERENCES manufacturers(manufacturer_id),

        CONSTRAINT fk_vehicle_dealer
            FOREIGN KEY (dealer_id)
            REFERENCES dealers(dealer_id),

        CONSTRAINT fk_vehicle_customer
            FOREIGN KEY (customer_id)
            REFERENCES customers(customer_id)
    )
""")


# --------------------------------------------------
# 5. Payments
# --------------------------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INT AUTO_INCREMENT PRIMARY KEY,

        vehicle_id INT NOT NULL,
        customer_id INT NOT NULL,

        payment_date DATE NOT NULL,

        payment_method VARCHAR(50) NOT NULL,

        amount DECIMAL(12,2) NOT NULL,

        payment_status VARCHAR(30) NOT NULL,

        transaction_reference VARCHAR(100),

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        CONSTRAINT fk_payment_vehicle
            FOREIGN KEY (vehicle_id)
            REFERENCES vehicles(vehicle_id),

        CONSTRAINT fk_payment_customer
            FOREIGN KEY (customer_id)
            REFERENCES customers(customer_id)
    )
""")


# --------------------------------------------------
# Commit changes
# --------------------------------------------------

connection.commit()


# --------------------------------------------------
# Verify tables
# --------------------------------------------------

cursor.execute("SHOW TABLES")

print("\nTables created successfully:\n")

for table in cursor.fetchall():
    print(table[0])


# --------------------------------------------------
# Close connection
# --------------------------------------------------

cursor.close()
connection.close()

print("\nDatabase setup completed successfully.")