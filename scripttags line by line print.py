from bs4 import BeautifulSoup
import json

with open("/mnt/c/Users/satya/Downloads/BestbuyHTML.txt", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

script_tags = soup.find_all('script')

for i, script_tag in enumerate(script_tags):
    print(f"\nScript Tag {i+1}:")
    if script_tag.string: 
        script_content = script_tag.string.strip()
        for line in script_content.split("\n"):
            print(line.strip())
    else:
        print("No text content in this <script> tag.")

