import pandas as pd
import random
import string
from uuid import uuid4
from datetime import datetime, timedelta

# Helper functions
def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_phone():
    # Generate a valid 10-digit phone number starting with non-zero digits
    while True:
        phone_number = ''.join(random.choices(string.digits, k=10))
        if len(phone_number) == 10 and phone_number[0] != '0':  # Ensure 10 digits and no leading zero
            return phone_number

def random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31, 23, 59, 59)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)  # seconds in a day
    return (start_date + timedelta(days=random_days, seconds=random_seconds)).strftime('%Y-%m-%d %H:%M:%S')

# Define U.S. state codes
us_state_codes = ['TX', 'CA', 'AZ', 'NY', 'FL', 'PA', 'IL', 'OH', 'GA', 'NC']

# Task 1: Create table1
data_table1 = {
    "name": [random_string(3) for _ in range(1000)],
    "age": [random.randint(10, 99) for _ in range(1000)],
    "city": [random_string(5) for _ in range(1000)],
    "zipcode": [random.randint(10000, 99999) for _ in range(1000)],
    "phone": [random_phone() for _ in range(1000)],
    "state_code": [random.choice(us_state_codes) for _ in range(1000)],  # Use only valid U.S. state codes
    "order_id": [str(uuid4()) for _ in range(1000)]
}
df_table1 = pd.DataFrame(data_table1)

# Task 2: Create table2
data_table2 = {
    "state_code": df_table1["state_code"],  # Ensure the state_codes in table2 match table1
    "County": [random_string(6) for _ in range(1000)],
    "order_date": [random_date(2020, 2024) for _ in range(1000)],
    "phone": df_table1["phone"],  # Ensure the phone numbers in table2 match table1
    "order_id": [str(uuid4()) for _ in range(1000)],
    "name": df_table1["name"]  # Ensure the names in table2 match table1
}
df_table2 = pd.DataFrame(data_table2)

# Update file paths to your desired directory
file_path_table1 = "C:\\Users\\satya\\Downloads\\table1.csv"
file_path_table2 = "C:\\Users\\satya\\Downloads\\table2.csv"

# Save to CSV files
df_table1.to_csv(file_path_table1, index=False)
df_table2.to_csv(file_path_table2, index=False)

print(f"Files created:\n- {file_path_table1}\n- {file_path_table2}")
