import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/gp/offer-listing/B00X4WHP5E/ref=dp_olp_new_mbc?ie=UTF8&condition=new")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "a-size-large"})

string_price = element.text.strip()
price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if price < 200:
    print("You should buy the speakers.")
    print("The current price is: {}".format(string_price))
else:
    print("Do not buy the speakers. They are to expensive.")


