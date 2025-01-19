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

# Define U.S. state codes and corresponding cities, counties, and zip codes
us_states = {
    'TX': {
        'cities': ['Austin', 'Dallas', 'Houston', 'San Antonio', 'Fort Worth'],
        'counties': ['Harris', 'Dallas', 'Tarrant', 'Bexar', 'Travis', 'Collin'],
        'zipcodes': {'Austin': '73301', 'Dallas': '75201', 'Houston': '77001', 'San Antonio': '78201', 'Fort Worth': '76101'}
    },
    'CA': {
        'cities': ['Los Angeles', 'San Francisco', 'San Diego', 'Sacramento', 'San Jose'],
        'counties': ['Los Angeles', 'San Diego', 'Orange', 'Riverside', 'Sacramento', 'Alameda'],
        'zipcodes': {'Los Angeles': '90001', 'San Francisco': '94102', 'San Diego': '92101', 'Sacramento': '95814', 'San Jose': '95101'}
    },
    'AZ': {
        'cities': ['Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Glendale'],
        'counties': ['Maricopa', 'Pima', 'Pinal', 'Yavapai', 'Coconino', 'Navajo'],
        'zipcodes': {'Phoenix': '85001', 'Tucson': '85701', 'Mesa': '85201', 'Chandler': '85224', 'Glendale': '85301'}
    },
    'NY': {
        'cities': ['New York City', 'Buffalo', 'Rochester', 'Syracuse', 'Albany'],
        'counties': ['Kings', 'Queens', 'New York', 'Bronx', 'Suffolk', 'Monroe'],
        'zipcodes': {'New York City': '10001', 'Buffalo': '14201', 'Rochester': '14602', 'Syracuse': '13202', 'Albany': '12201'}
    },
    'FL': {
        'cities': ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee'],
        'counties': ['Miami-Dade', 'Broward', 'Palm Beach', 'Hillsborough', 'Orange', 'Duval'],
        'zipcodes': {'Miami': '33101', 'Orlando': '32801', 'Tampa': '33601', 'Jacksonville': '32202', 'Tallahassee': '32301'}
    },
    'PA': {
        'cities': ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading'],
        'counties': ['Philadelphia', 'Allegheny', 'Montgomery', 'Bucks', 'Delaware', 'Chester'],
        'zipcodes': {'Philadelphia': '19102', 'Pittsburgh': '15201', 'Allentown': '18102', 'Erie': '16501', 'Reading': '19601'}
    },
    'IL': {
        'cities': ['Chicago', 'Aurora', 'Naperville', 'Joliet', 'Rockford'],
        'counties': ['Cook', 'DuPage', 'Lake', 'Will', 'Kane', 'McHenry'],
        'zipcodes': {'Chicago': '60601', 'Aurora': '60502', 'Naperville': '60540', 'Joliet': '60431', 'Rockford': '61101'}
    },
    'OH': {
        'cities': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron'],
        'counties': ['Cuyahoga', 'Franklin', 'Hamilton', 'Summit', 'Montgomery', 'Medina'],
        'zipcodes': {'Columbus': '43201', 'Cleveland': '44101', 'Cincinnati': '45202', 'Toledo': '43601', 'Akron': '44301'}
    },
    'GA': {
        'cities': ['Atlanta', 'Augusta', 'Columbus', 'Macon', 'Savannah'],
        'counties': ['Fulton', 'Gwinnett', 'Cobb', 'DeKalb', 'Chatham', 'Richmond'],
        'zipcodes': {'Atlanta': '30301', 'Augusta': '30901', 'Columbus': '31901', 'Macon': '31201', 'Savannah': '31401'}
    },
    'NC': {
        'cities': ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston-Salem'],
        'counties': ['Mecklenburg', 'Wake', 'Guilford', 'Durham', 'Forsyth', 'Cumberland'],
        'zipcodes': {'Charlotte': '28202', 'Raleigh': '27601', 'Greensboro': '27401', 'Durham': '27701', 'Winston-Salem': '27101'}
    }
}

# Filter cities to include only those with a max of 5 letters
for state in us_states.values():
    state['cities'] = [city for city in state['cities'] if len(city) <= 5]

# Filter counties to include only those with a max of 6 letters
for state in us_states.values():
    state['counties'] = [county for county in state['counties'] if len(county) <= 6]

# Ensure that at least one city is available in each state
for state in us_states.values():
    if not state['cities']:
        state['cities'] = ['Austn']  # Default valid city for the state

# Task 1: Create table1
data_table1 = {
    "name": [random_string(3) for _ in range(1000)],
    "age": [random.randint(10, 99) for _ in range(1000)],
    "state_code": [random.choice(list(us_states.keys())) for _ in range(1000)],  # Ensure only valid U.S. state codes
}

# Select a matching city and zip code for each state
data_table1["city"] = [random.choice(us_states[state]['cities']) for state in data_table1["state_code"]]
data_table1["zipcode"] = [us_states[state]['zipcodes'].get(city, '58696') for state, city in zip(data_table1["state_code"], data_table1["city"])]
data_table1["phone"] = [random_phone() for _ in range(1000)]
data_table1["order_id"] = [str(uuid4()) for _ in range(1000)]

df_table1 = pd.DataFrame(data_table1)

# Task 2: Create table2
data_table2 = {
    "state_code": df_table1["state_code"],  # Ensure the state_codes in table2 match table1
    "County": [random.choice(us_states[state]['counties']) for state in df_table1["state_code"]],  # Match counties with the state_code (max 6 counties)
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
