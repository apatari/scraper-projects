from bs4 import BeautifulSoup
import requests

url = "https://www.blackdiamondequipment.com/en_US/product/8-5-dry-climbing-rope-past-season/?sku=BD323015GREN0501&gad_source=1&gclid=CjwKCAjwzN-vBhAkEiwAYiO7oHjuTDVGYYYGkxDgJkD0cAtXiLqGRkxzjs8Pvy_qAKknKjY2NHQTDRoC_VQQAvD_BwE&gclsrc=aw.ds"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")


prices = doc.find_all(class_="low-sale-price")

print(prices[0].text)