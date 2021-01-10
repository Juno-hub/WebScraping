from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
)

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
ua = browser.find_element_by_id("detected_value").text
print(ua)

browser.quit()