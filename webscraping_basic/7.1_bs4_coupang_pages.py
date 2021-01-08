import re
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

for i in range(1, 6):
    # print("Page:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(
        i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:

        # Except for advertising product
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()
        # Except for Apple product
        if "Apple" in name:
            continue

        price = item.find("strong", attrs={"class": "price-value"}).get_text()

        # 리뷰 100개 이상, 평점 4.5 이상인 상품만 조회
        rate = item.find("em", attrs={"class": "rating"})
        rate_cnt = item.find("span", attrs={"class": "rating-total-count"})
        if rate:
            rate = rate.get_text()
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            # print(name, price, rate, rate_cnt)
            print(f"Name: {name}")
            print(f"Price: {price}")
            print(f"Rate: {rate}({rate_cnt})")
            print("Move to: https://www.coupang.com{}".format(link))
            print("=" * 50)
