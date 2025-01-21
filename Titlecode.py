from bs4 import BeautifulSoup

# Open and read the HTML file
with open("BestbuyHTML.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Extract the title tag
title_tag = soup.title

if title_tag:
    print("Title tag:", title_tag)
    print("Title text:", title_tag.string)
else:
    print("No title tag found in the HTML file.")
