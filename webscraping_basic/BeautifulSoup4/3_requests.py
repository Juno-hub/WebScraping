import requests
# res = requests.get("https://www.naver.com")
# res = requests.get("https://nadocoding.tistory.com")
res = requests.get("https://www.google.com")
res.raise_for_status()

# # if res.status_code == 200:
# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다.[Error code", res.statues_code, "]")
with open("my_google.html", "w", encoding="utf8") as f:
    f.write(res.text)