from bs4 import BeautifulSoup

with open("/mnt/c/Users/satya/Downloads/BestbuyHTML.txt", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

title_tag = soup.title

if title_tag:
    print("Title tag:", title_tag)
    print("Title text:", title_tag.string)
else:
    print("No title tag found in the HTML file.")
