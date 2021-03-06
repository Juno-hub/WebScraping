import re
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).get_text())

for item in items:

    # Except for advertising product
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        # print(" <Except for advertising product> ")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()
    # Except for Apple product
    if "Apple" in name:
        # print(" <Except for Apple product>")
        continue

    price = item.find("strong", attrs={"class": "price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5 이상인 상품만 조회
    rate = item.find("em", attrs={"class": "rating"})
    rate_cnt = item.find("span", attrs={"class": "rating-total-count"})
    if rate:
        rate = rate.get_text()
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
        # print("Review:", rate_cnt)
    else:
        # rate = "No Rate"
        # rate_cnt = "No the number of rate"
        # print(" <Except for having not a rate> ")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
