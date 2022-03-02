import requests
import re
from bs4 import BeautifulSoup

url = "https://distiller.com/profile/duggifresh/tastes"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":"taste user-taste js-carousel whiskey-content"})

for item in items:
    name = item.find("h3", attrs={"class":"mini-headline name truncate-line"}).get_text()
    score = item.find("div", attrs={"class":"rating-display__value"}).get_text()
    print("Name : ", name)
    print("Rate : ", score)