from selenium import webdriver


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# headlessChrome을 쓸 경우 브라우저에서 막는 경우가 생김
# 따라서 headless 쓸 경우에는 기존 user-agent를 지정해 줄 필요가 있음
# 기존 user-agent를 지정해 줄 경우에는 headless로 인식되지 않음

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()


url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

'''
Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/92.0.4515.131 Safari/537.36
'''

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# headless Chrome 일 경우
'''
Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
AppleWebKit/537.36 (KHTML, like Gecko) 
HeadlessChrome/92.0.4515.131 Safari/537.36'''