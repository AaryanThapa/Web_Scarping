import requests
import pandas as pd
from lxml import html
import os
url = "https://books.toscrape.com/catalogue/under-the-tuscan-sun_504/index.html"

r = requests.get(url, timeout=20)

print("Status Code:", r.status_code)

tree = html.fromstring(r.content)

# put everything in one dictionary
book = {}

book["Title"] = tree.xpath('//h1/text()')[0]
book["Price"] = tree.xpath('//p[@class="price_color"]/text()')[0]
book["Rating"] = tree.xpath(
    '//p[contains(@class,"star-rating")]/@class')[0].replace("star-rating", "").strip()

desc = tree.xpath(
    '//div[@id="product_description"]/following-sibling::p/text()')
book["Description"] = desc[0] if desc else ""

rows = tree.xpath('//table[@class="table table-striped"]//tr')

for row in rows:
    name = row.xpath('.//th/text()')[0]
    value = row.xpath('.//td/text()')[0]
    book[name] = value

df = pd.DataFrame([book])
file_exists=os.path.exists("book.csv")

df.to_csv("book.csv",mode="a",header=not file_exists, index=False, encoding="utf-8-sig")

print(df)
print("Saved to book.csv")
