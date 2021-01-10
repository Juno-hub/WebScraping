# Quiz) 부동산 매물, 송파 헬리오시티 정보를 스크래핑 하는 프로그램을 만드시오.

# [조회 조건]
# 1. https://www.daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# =========== 매물 1 ===========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# =========== 매물 2 ===========
# ...
# [주의사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://www.daum.net")

elem = browser.find_element_by_id("q")
elem.send_keys("송파 헬리오시티")
elem.send_keys(Keys.ENTER)

for i in range(1, 6):
    item = " 매물 {} ".format(i)
    deal = browser.find_element_by_xpath(
        f'//*[@id="estateCollTabContentsResult"]/div/table/tbody/tr[{i}]/td[1]/div'
    ).text
    area = browser.find_element_by_xpath(
        f'//*[@id="estateCollTabContentsResult"]/div/table/tbody/tr[{i}]/td[2]/div'
    ).text
    price = browser.find_element_by_xpath(
        f'//*[@id="estateCollTabContentsResult"]/div/table/tbody/tr[{i}]/td[3]/div'
    ).text
    number = browser.find_element_by_xpath(
        f'//*[@id="estateCollTabContentsResult"]/div/table/tbody/tr[{i}]/td[4]/div'
    ).text
    floor = browser.find_element_by_xpath(
        f'//*[@id="estateCollTabContentsResult"]/div/table/tbody/tr[{i}]/td[5]/div'
    ).text

    print("{0:=^28}".format(item))
    print("거래 :", deal)
    print("면적 :", area, "(공급/전용)")
    print("가격 :", price, "(만원)")
    print("동 :", number)
    print("층 :", floor)

    # Debriefing
    # Selenium is slower than Requests and BeautifulSoup4
    # When you make HTML file by BeautifulSoup, if the file doesn't have the element you want to find, then you use Selenium.
