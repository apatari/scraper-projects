from bs4 import BeautifulSoup
import requests

url = f"https://www.backcountry.com/search?s=u&q=helmet"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

pages = [int(page.text) for page in doc.find_all("a", attrs={"data-id": "pageItem"})]

print(max(pages))
for page in pages:
    print(page)