import requests

# 403 error는 페이지 접근 권한이 없는 경우이다. 그래서 403 에러가 뜨면 User-Agent를 지정해주어야 한다.
url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)