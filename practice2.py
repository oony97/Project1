import requests
import re
from bs4 import BeautifulSoup

count = 0 # 아이템 번호

# 페이지 1에서 10까지의 리뷰 가져오기
for i in range(1, 11):
    url = "https://distiller.com/profile/stinkybatt/tastes?page={}".format(i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":"taste user-taste js-carousel whiskey-content"})

    for item in items:
        count += 1
        name = item.find("h3", attrs={"class":"mini-headline name truncate-line"}).get_text()
        score = item.find("div", attrs={"class":"rating-display__value"}).get_text()
        print("#" + str(count))
        print("Name : ", name)
        print("Rate : ", score)
    print("<Next Page>")

