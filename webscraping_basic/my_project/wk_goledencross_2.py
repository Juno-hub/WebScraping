import time
from selenium import webdriver

browser = webdriver.Chrome()
# KRX 일자별 시세
url = "http://marketdata.krx.co.kr/mdi#document=040204"
browser.get(url)

# 1개월 버튼 클릭
btn_oneMonth = browser.find_element_by_xpath(
    '//*[@id="formc81e728d9d4c2f636f067f89cc14862c"]/dl[2]/dd/div/button[3]')
btn_oneMonth.click()

time.sleep(2)

# 조회 버튼 클릭
btn_search = browser.find_element_by_xpath(
    '//*[@id="btnidc81e728d9d4c2f636f067f89cc14862c"]')
btn_search.click()

time.sleep(2)

# 5MA 구하기
five_total = 0
for i in range(1, 6):
    closing_price = browser.find_element_by_xpath(
        f'//*[@id="area45c48cce2e2d7fbdea1afc51c7c6ad26"]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td[2]'
    ).text
    closing_price = int(closing_price.replace(",", ""))
    five_total += closing_price
five_MA = five_total / 5
print("5MA:", five_MA)

# 10MA 구하기
ten_total = 0
for i in range(1, 11):
    closing_price = browser.find_element_by_xpath(
        f'//*[@id="area45c48cce2e2d7fbdea1afc51c7c6ad26"]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td[2]'
    ).text
    closing_price = int(closing_price.replace(",", ""))
    ten_total += closing_price
ten_MA = ten_total / 10
print("10MA:", ten_MA)
