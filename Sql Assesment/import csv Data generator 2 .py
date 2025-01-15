import csv
import random
import uuid
from datetime import datetime, timedelta

# Random Data Generation Helpers
def generate_name():
    first_names = ["John", "Jane", "Emily", "Chris", "Alex", "Taylor", "Jordan", "Morgan", "Cameron", "Jessie"]
    last_names = ["Adams", "Baker", "Clark", "Evans", "Foster", "Gomez", "Hughes", "Ibarra", "Johnson", "King"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_state_code():
    state_codes = ["WA", "TX", "MA", "CO", "GA", "CA", "FL", "NV", "OR", "NY"]
    return random.choice(state_codes)

def generate_county():
    counties = ["King", "Harris", "Maricopa", "Los Angeles", "Cook", "San Diego", "Miami-Dade", "Cuyahoga", "San Bernardino", "Dallas"]
    return random.choice(counties)

def generate_order_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    time_difference = end_date - start_date
    random_days = random.randint(0, time_difference.days)
    random_time = random.randint(0, 86399)  # 24 hours * 60 minutes * 60 seconds - random second of the day
    order_date = start_date + timedelta(days=random_days, seconds=random_time)
    return order_date.strftime("%Y-%m-%d %H:%M:%S")

def generate_phone():
    area_code = random.randint(200, 999)  # Area code between 200 and 999
    exchange_code = random.randint(200, 999)  # Exchange code between 200 and 999
    line_number = random.randint(1000, 9999)  # Line number between 1000 and 9999
    return f"{area_code}-{exchange_code}-{line_number}"

def generate_order_id():
    return str(uuid.uuid4())  # Generate a UUID for order ID

# Open CSV file for writing
with open('addresstable2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["state_code", "County", "order_date", "phone", "order_id", "name"])  # Write header
    
    # Generate 1000 rows of random data
    for _ in range(1000):
        writer.writerow([
            generate_state_code(),
            generate_county(),
            generate_order_date(),
            generate_phone(),
            generate_order_id(),
            generate_name()
        ])
