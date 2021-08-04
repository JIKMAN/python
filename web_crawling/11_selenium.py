from selenium import webdriver
import time

browser = webdriver.Chrome("../chromedriver.exe")
# 브라우저로 이동
browser.get("http://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 로그인
browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("pw").send_keys("my_password")
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 틀린 아이디 지우기
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("id")
browser.find_element_by_id("pw").send_keys("pw")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
# browser.close() # 현재 탭
browser.quit() # 전체

# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#     e.get_attribute("href")

# browser.back()
# elem = browser.find_element_by_xpath("//*[@id='search_btn']")
# elem.click()

# # 브라우저 현재 탭 종료
# # browser.close()

# # 브라우저 전체 종료
# browser.quit()