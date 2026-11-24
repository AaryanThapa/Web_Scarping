import requests
import pandas as pd
from lxml import html

url = "https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html"

r = requests.get(url, timeout=20)

print("Status Code:", r.status_code)

tree = html.fromstring(r.content)

# put everything in one dictionary
book = {}

book["Title"] = tree.xpath('//h1/text()')[0]
book["Price"] = tree.xpath('//p[@class="price_color"]/text()')[0]
book["Rating"] = tree.xpath('//p[contains(@class,"star-rating")]/@class')[0].replace("star-rating", "").strip()

desc = tree.xpath('//div[@id="product_description"]/following-sibling::p/text()')
book["Description"] = desc[0] if desc else ""

# the table at the bottom (UPC, availability, reviews...)
rows = tree.xpath('//table[@class="table table-striped"]//tr')

for row in rows:
    name = row.xpath('.//th/text()')[0]
    value = row.xpath('.//td/text()')[0]
    book[name] = value

# one book = one row
df = pd.DataFrame([book])

df.to_csv("book.csv", index=False, encoding="utf-8-sig")

print(df)
print("Saved to book.csv")