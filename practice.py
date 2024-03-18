from bs4 import BeautifulSoup
import requests

url = "https://www.backcountry.com/search?s=u&q=rope"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")


prices = doc.find_all(attrs={"data-id":"productListingPrice"})

highPrice = prices[0].find("span")

print(highPrice.text)