from bs4 import BeautifulSoup
import json

# Load the HTML file
with open('BestbuyHTML.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <script> tags
script_tags = soup.find_all('script')

# Loop through each script tag
for script in script_tags:
    if script.string:  # Ensure the script tag contains text
        try:
            # Attempt to load as JSON
            json_data = json.loads(script.string)
            print("JSON Content from <script> tag:")
            # Print JSON content line by line
            for key, value in json_data.items():
                print(f"{key}: {value}")
        except json.JSONDecodeError:
            # Skip non-JSON content
            print("Non-JSON <script> tag encountered, skipping.")
