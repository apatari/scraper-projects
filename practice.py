from bs4 import BeautifulSoup
import requests

url = "https://www.backcountry.com/search?s=u&q=rope"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

def stripPrice(price):
    return (float(price.strip("$")))

prices = doc.find_all(attrs={"data-id":"productListingPrice"})

res = []

for price in prices:
    name = price.parent.parent.parent.find("h2", attrs={"data-id": "productListingTitle"})

    highPrice = price.find("span")
    res.append({"name": name.text, "price":highPrice.text})

res.sort(key=lambda item: stripPrice(item['price']))



filteredResults = [item for item in res if stripPrice(item['price']) < 300 ]

for item in filteredResults:
    print(item)