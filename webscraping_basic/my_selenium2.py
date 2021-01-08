from selenium import webdriver

browser = webdriver.Chrome()
# 1. 네이버로 이동
browser.get("https://www.naver.com/")
# 2. 로그인 버튼 찾기
elem = browser.find_element_by_class_name("link_login")
elem.click()
# 3. ID, PW 입력
browser.find_element_by_id("id").send_keys("naverId")
browser.find_element_by_id("pw").send_keys("password")
# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
# 5. ID 재입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")
# 6. HTML 정보 출력
print(browser.page_source)
# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료