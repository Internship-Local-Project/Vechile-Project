import random
from datetime import date, timedelta

import mysql.connector
from faker import Faker


# ============================================================
# CONFIGURATION
# ============================================================

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "D2_92672Pranay",
    "password": "manager",
    "database": "vehicle_legacy"
}

NUM_MANUFACTURERS = 20
NUM_DEALERS = 50
NUM_CUSTOMERS = 10000
NUM_VEHICLES = 20000
NUM_PAYMENTS = 15000


fake = Faker("en_IN")
random.seed(42)


# ============================================================
# CONNECT TO MYSQL
# ============================================================

connection = mysql.connector.connect(**DB_CONFIG)

cursor = connection.cursor()


print("Connected to MySQL successfully.")


# ============================================================
# HELPER FUNCTION
# ============================================================

def random_date(start_date, end_date):
    days = (end_date - start_date).days
    return start_date + timedelta(days=random.randint(0, days))


# ============================================================
# 1. MANUFACTURERS
# ============================================================

manufacturers = [
    ("Tata Motors", "India", 1945, "Mumbai"),
    ("Mahindra", "India", 1945, "Mumbai"),
    ("Maruti Suzuki", "India", 1981, "New Delhi"),
    ("Hyundai", "South Korea", 1967, "Seoul"),
    ("Toyota", "Japan", 1937, "Toyota City"),
    ("Honda", "Japan", 1948, "Tokyo"),
    ("Kia", "South Korea", 1944, "Seoul"),
    ("Volkswagen", "Germany", 1937, "Wolfsburg"),
    ("BMW", "Germany", 1916, "Munich"),
    ("Mercedes-Benz", "Germany", 1926, "Stuttgart"),
    ("Audi", "Germany", 1909, "Ingolstadt"),
    ("Ford", "USA", 1903, "Dearborn"),
    ("Tesla", "USA", 2003, "Austin"),
    ("Nissan", "Japan", 1933, "Yokohama"),
    ("Renault", "France", 1899, "Boulogne-Billancourt"),
    ("Skoda", "Czech Republic", 1895, "Mlada Boleslav"),
    ("MG Motor", "UK", 1924, "London"),
    ("Jeep", "USA", 1941, "Auburn Hills"),
    ("Volvo", "Sweden", 1927, "Gothenburg"),
    ("Jaguar", "UK", 1935, "Whitley")
]

manufacturer_ids = []

for manufacturer in manufacturers:

    cursor.execute("""
        INSERT INTO manufacturers
        (
            manufacturer_name,
            country,
            founded_year,
            headquarters
        )
        VALUES (%s, %s, %s, %s)
    """, manufacturer)

    manufacturer_ids.append(cursor.lastrowid)


print(f"Inserted {len(manufacturer_ids)} manufacturers.")


# ============================================================
# 2. DEALERS
# ============================================================

dealer_ids = []

dealer_names = [
    "Prime Motors",
    "City Auto",
    "Metro Motors",
    "Elite Automobiles",
    "Highway Motors",
    "Capital Cars",
    "Auto World",
    "Royal Motors",
    "Star Automobiles",
    "United Motors"
]

indian_cities = [
    ("Pune", "Maharashtra"),
    ("Mumbai", "Maharashtra"),
    ("Nagpur", "Maharashtra"),
    ("Nashik", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Bengaluru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Ahmedabad", "Gujarat"),
    ("Kolkata", "West Bengal"),
    ("Jaipur", "Rajasthan"),
    ("Surat", "Gujarat"),
    ("Indore", "Madhya Pradesh"),
    ("Bhopal", "Madhya Pradesh"),
    ("Lucknow", "Uttar Pradesh")
]

for i in range(NUM_DEALERS):

    city, state = random.choice(indian_cities)

    dealer_name = f"{random.choice(dealer_names)} {i + 1}"

    cursor.execute("""
        INSERT INTO dealers
        (
            dealer_name,
            city,
            state,
            address,
            phone,
            email,
            dealer_type,
            opening_date
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        dealer_name,
        city,
        state,
        fake.street_address(),
        fake.phone_number(),
        f"dealer{i + 1}@vehiclecompany.com",
        random.choice(["Authorized", "Premium", "Standard"]),
        random_date(date(2000, 1, 1), date(2024, 12, 31))
    ))

    dealer_ids.append(cursor.lastrowid)


print(f"Inserted {len(dealer_ids)} dealers.")


# ============================================================
# 3. CUSTOMERS
# ============================================================

customer_ids = []

for i in range(NUM_CUSTOMERS):

    first_name = fake.first_name()
    last_name = fake.last_name()

    cursor.execute("""
        INSERT INTO customers
        (
            first_name,
            last_name,
            email,
            phone,
            date_of_birth,
            city,
            state,
            registration_date
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        first_name,
        last_name,
        f"{first_name.lower()}.{last_name.lower()}{i}@example.com",
        fake.phone_number(),
        fake.date_of_birth(
            minimum_age=21,
            maximum_age=70
        ),
        fake.city(),
        fake.state(),
        random_date(
            date(2018, 1, 1),
            date(2026, 8, 1)
        )
    ))

    customer_ids.append(cursor.lastrowid)

    if (i + 1) % 1000 == 0:
        print(f"Customers inserted: {i + 1}")


print(f"Inserted {len(customer_ids)} customers.")


# ============================================================
# 4. VEHICLES
# ============================================================

vehicle_ids = []

vehicle_models = [
    ("Nexon", "SUV", "Petrol", "Manual"),
    ("Nexon EV", "SUV", "Electric", "Automatic"),
    ("Punch", "SUV", "Petrol", "Manual"),
    ("Harrier", "SUV", "Diesel", "Automatic"),
    ("XUV700", "SUV", "Diesel", "Automatic"),
    ("Scorpio", "SUV", "Diesel", "Manual"),
    ("Thar", "SUV", "Diesel", "Manual"),
    ("Creta", "SUV", "Petrol", "Automatic"),
    ("Venue", "SUV", "Petrol", "Manual"),
    ("Verna", "Sedan", "Petrol", "Automatic"),
    ("Swift", "Hatchback", "Petrol", "Manual"),
    ("Baleno", "Hatchback", "Petrol", "Automatic"),
    ("Fortuner", "SUV", "Diesel", "Automatic"),
    ("Camry", "Sedan", "Hybrid", "Automatic"),
    ("City", "Sedan", "Petrol", "Automatic"),
    ("Civic", "Sedan", "Petrol", "Automatic"),
    ("Seltos", "SUV", "Petrol", "Automatic"),
    ("Sonet", "SUV", "Diesel", "Manual"),
    ("Virtus", "Sedan", "Petrol", "Automatic"),
    ("Model 3", "Sedan", "Electric", "Automatic")
]

colors = [
    "White",
    "Black",
    "Silver",
    "Red",
    "Blue",
    "Grey"
]

statuses = [
    "AVAILABLE",
    "SOLD"
]

for i in range(NUM_VEHICLES):

    manufacturer_id = random.choice(manufacturer_ids)
    dealer_id = random.choice(dealer_ids)

    model_name, vehicle_type, fuel_type, transmission = random.choice(
        vehicle_models
    )

    status = random.choices(
        statuses,
        weights=[30, 70]
    )[0]

    if status == "SOLD":

        customer_id = random.choice(customer_ids)

        sale_date = random_date(
            date(2020, 1, 1),
            date(2026, 8, 10)
        )

    else:

        customer_id = None
        sale_date = None

    price = random.randint(
        500000,
        5000000
    )

    vin = fake.unique.bothify(
        text="?????????????????"
    ).upper()

    cursor.execute("""
        INSERT INTO vehicles
        (
            manufacturer_id,
            dealer_id,
            customer_id,
            vin,
            model_name,
            vehicle_type,
            fuel_type,
            transmission,
            manufacturing_year,
            color,
            price,
            sale_date,
            vehicle_status
        )
        VALUES
        (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s
        )
    """, (
        manufacturer_id,
        dealer_id,
        customer_id,
        vin,
        model_name,
        vehicle_type,
        fuel_type,
        transmission,
        random.randint(2018, 2026),
        random.choice(colors),
        price,
        sale_date,
        status
    ))

    vehicle_ids.append({
        "vehicle_id": cursor.lastrowid,
        "customer_id": customer_id,
        "status": status,
        "price": price,
        "sale_date": sale_date
    })

    if (i + 1) % 1000 == 0:
        print(f"Vehicles inserted: {i + 1}")


print(f"Inserted {len(vehicle_ids)} vehicles.")


# ============================================================
# 5. PAYMENTS
# ============================================================

sold_vehicles = [
    vehicle
    for vehicle in vehicle_ids
    if vehicle["status"] == "SOLD"
    and vehicle["customer_id"] is not None
]

random.shuffle(sold_vehicles)

payment_count = min(
    NUM_PAYMENTS,
    len(sold_vehicles)
)

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Bank Transfer",
    "Loan"
]

payment_statuses = [
    "COMPLETED",
    "COMPLETED",
    "COMPLETED",
    "PENDING",
    "FAILED"
]

for i in range(payment_count):

    vehicle = sold_vehicles[i]

    vehicle_price = vehicle["price"]

    # Generate a realistic payment amount.
    amount = round(
        vehicle_price * random.uniform(0.10, 0.50),
        2
    )

    payment_date = vehicle["sale_date"]

    if payment_date is None:
        payment_date = date.today()

    cursor.execute("""
        INSERT INTO payments
        (
            vehicle_id,
            customer_id,
            payment_date,
            payment_method,
            amount,
            payment_status,
            transaction_reference
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s)
    """, (
        vehicle["vehicle_id"],
        vehicle["customer_id"],
        payment_date,
        random.choice(payment_methods),
        amount,
        random.choice(payment_statuses),
        f"TXN-{random.randint(100000000, 999999999)}"
    ))

    if (i + 1) % 1000 == 0:
        print(f"Payments inserted: {i + 1}")


print(f"Inserted {payment_count} payments.")


# ============================================================
# COMMIT
# ============================================================

connection.commit()

print("\n========================================")
print("DATA GENERATION COMPLETED")
print("========================================")

# ============================================================
# VERIFY DATA
# ============================================================

tables = [
    "manufacturers",
    "dealers",
    "customers",
    "vehicles",
    "payments"
]

print("\nRecord counts:")

for table in tables:

    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(f"{table:20} {count:,}")


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
connection.close()

print("\nMySQL connection closed.")