from bs4 import BeautifulSoup
import requests

def bcSearcher(param, max):

    url = f"https://www.backcountry.com/search?s=u&q={param}"
    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")

    # def stripPrice(price):
    #     try:
    #         return (float(price.strip("$")))
    #     except:
    #         return 0 

    prices = doc.find_all(attrs={"data-id":"productListingPrice"})

    res = []

    for price in prices:
        name = price.parent.parent.parent.find("h2", attrs={"data-id": "productListingTitle"})

        priceString = price.find_all(class_="chakra-text")[0].contents[-1]
        priceFloat = float(priceString.strip("$"))

        res.append({"name": name.text, "priceString":priceString, "priceFloat":priceFloat})

    res.sort(key=lambda item: (item['priceFloat']))



    filteredResults = [item for item in res if item['priceFloat'] < max ]

    return filteredResults


# url = f"https://www.backcountry.com/search?s=u&q=helmet"
# result = requests.get(url)

# doc = BeautifulSoup(result.text, "html.parser")
# prices = doc.find_all(attrs={"data-id":"productListingPrice"})

# res = []

# priceString = prices[2].find_all(class_="chakra-text")[0].contents[-1]
# priceFloat = float(priceString.strip("$"))

# print(priceFloat)


# print(float(test[0].contents[-1].strip("$")))
