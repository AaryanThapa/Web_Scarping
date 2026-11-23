import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.yellowpagesnepal.com/"

r = requests.get(url, timeout=20)

soup = BeautifulSoup(r.content, "html.parser")

# Find only the required anchor tag
element = soup.select_one('a[href="agriculture-and-handicraft"]')

if element:
    text = element.get_text(strip=True)
    href = element.get("href")

    with open("agriculture.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Category Name", "Category URL"])
        writer.writerow([text, href])

    print("Data saved successfully!")
else:
    print("Required anchor tag not found.")