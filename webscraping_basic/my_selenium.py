from selenium import webdriver

browser = webdriver.Chrome()  # "../chromedriver.exe"
browser.get("https://www.naver.com/")

# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()
# elem = browser.find_element_by_id("query")
# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)