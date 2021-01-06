import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=602910&weekday=mon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# webtoons = soup.find_all("td", attrs={"class": "title"})
# title = webtoons[0].a.get_text()
# link = webtoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
# for webtoon in webtoons:
#     title = webtoon.a.get_text()
#     link = "https://comic.naver.com" + webtoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0
webtoon_rates = soup.find_all("div", attrs={"class": "rating_type"})
for webtoon_rate in webtoon_rates:
    rate = webtoon_rate.find("strong").get_text()
    total_rates += float(rate)
print("전체 점수:", total_rates)
print("평균 점수:", total_rates / len(webtoon_rates))
