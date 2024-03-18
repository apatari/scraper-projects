from bs4 import BeautifulSoup
import requests

url = "https://www.backcountry.com/search?s=u&q=rope"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")


prices = doc.find_all(attrs={"data-id":"productListingPrice"})

res = []

for price in prices:
    name = price.parent.parent.parent.find("h2", attrs={"data-id": "productListingTitle"})

    highPrice = price.find("span")
    res.append({"name": name.text, "price":highPrice.text})

res.sort(key=lambda item: item['price'])

for item in res:
    print(item)