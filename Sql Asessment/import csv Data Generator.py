import csv
import random
import uuid

# Random Data Generation Helpers
def generate_name():
    first_names = ["John", "Jane", "Emily", "Chris", "Alex"]
    last_names = ["Adams", "Baker", "Clark", "Evans", "Foster"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_age():
    return random.randint(18, 70)

def generate_city():
    cities = ["Seattle", "Austin", "Boston", "Denver", "Atlanta"]
    return random.choice(cities)

def generate_zipcode():
    return random.randint(10000, 99999)

def generate_phone():
    area_code = random.randint(200, 999)  # Area code between 200 and 999
    exchange_code = random.randint(200, 999)  # Exchange code between 200 and 999
    line_number = random.randint(1000, 9999)  # Line number between 1000 and 9999
    return f"{area_code}-{exchange_code}-{line_number}"

def generate_state_code():
    state_codes = ["WA", "TX", "MA", "CO", "GA"]
    return random.choice(state_codes)

def generate_order_id():
    return str(uuid.uuid4())

# Open CSV file for writing
with open('addresstable1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city", "zipcode", "phone", "state_code", "order_id"])  # Write header
    
    # Generate 1000 rows of random data
    for _ in range(1000):
        writer.writerow([
            generate_name(),
            generate_age(),
            generate_city(),
            generate_zipcode(),
            generate_phone(),  
            generate_state_code(),
            generate_order_id()
        ])
