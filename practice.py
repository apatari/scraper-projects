from bs4 import BeautifulSoup
import requests

def bcSearcher(param, max, min):

    url = f"https://www.backcountry.com/search?s=u&q={param}"
    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")

    prices = doc.find_all(attrs={"data-id":"productListingPrice"})

    res = []

    for price in prices:
        name = price.parent.parent.parent.find("h2", attrs={"data-id": "productListingTitle"})

        anchor = price.parent.parent.parent.parent.find("a", class_="chakra-linkbox__overlay")
        link = "https://www.backcountry.com" + anchor.attrs['href']

        priceString = price.find_all(class_="chakra-text")[0].contents[-1]
        priceFloat = float(priceString.strip("$").replace(",",""))

        res.append({"name": name.text, "priceString":priceString, "priceFloat":priceFloat, "link": link})

    res.sort(key=lambda item: (item['priceFloat']))

    filteredResults = [item for item in res if min <= item['priceFloat'] <= max ]

    return filteredResults

