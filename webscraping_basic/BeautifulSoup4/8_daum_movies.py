import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(
        year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    posters = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, poster in enumerate(posters):
        poster_url = poster["src"]
        if poster_url.startswith("//"):
            poster_url = "https:" + poster_url

        # print(poster_url)
        image_res = requests.get(poster_url)
        image_res.raise_for_status()

        with open("movie_{0}_{1}.jpg".format(year, idx + 1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:
            break