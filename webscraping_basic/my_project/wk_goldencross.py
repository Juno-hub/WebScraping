import time
from selenium import webdriver

browser = webdriver.Chrome()
# KRX 일자별 시세
url = "http://marketdata.krx.co.kr/mdi#document=040204"
browser.get(url)

# 종목검색 Default: 삼성전자
# 종목검색 창에서 입력값 = "A{종목코드}/{기업명}""
# 종목검색 버튼 클릭
# browser.find_element_by_name("finderbtn").click()

# time.sleep(3)

# 종목검색기 내에 종목 입력
# btn_q = browser.find_element_by_name("searchText")
# btn_q.click()
# btn_q.send_keys("005380")

# # 종목검색기 버튼 클릭[안 될 시 다시 활성화.]
# btn_item = browser.find_element_by_id("btnidc16a5320fa475530d9583c34fd356ef5")
# btn_item.click()

# 종목 클릭 및 기업명 추출
# browser.find_element_by_xpath(
#     '//*[@id="4e732ced3463d06de0ca9a15b6153677"]/div/dl/dd/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr/td[2]/a'
# ).click()

# time.sleep(3)

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

# 최근 10일 날짜 및 종가 출력
for i in range(1, 11):
    date = browser.find_element_by_xpath(
        f'//*[@id="area45c48cce2e2d7fbdea1afc51c7c6ad26"]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td[1]'
    ).text
    closing_price = browser.find_element_by_xpath(
        f'//*[@id="area45c48cce2e2d7fbdea1afc51c7c6ad26"]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td[2]'
    ).text
    # print(f"[{name}]")
    print("날짜: " + date, "종가: " + closing_price)
