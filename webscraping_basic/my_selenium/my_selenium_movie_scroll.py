# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
#     "Accept-Language": "ko-KR,ko"
# }
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
# # print(len(movies))

# # with open("movie.html", "w", encoding="utf8") as f:
# #     # f.write(res.text)
# #     f.write(soup.prettify())  # HTML 문서를 보기 좋게 정렬시켜줌.

# for movie in movies:
#     title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
#     print(title)

from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 해상도의 1080으로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")
# browser.execute_script("window.scrollTo(0,2080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time

interval = 2  # 2초마다 스크롤을 내림

# 현재 문서 높이를 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤를 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("스크롤 완료")