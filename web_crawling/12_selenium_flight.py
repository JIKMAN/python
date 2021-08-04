from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

browser.maximize_window() # 창 최대화

url = "https://beta-flight.naver.com/"
browser.get(url)

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "xpath값"))) # XPATH 말고 ID, CLASS등 다 사용 가능
    # 성공했을 때 동작 수행
    print(elem.text)
finally:
    browser.quit()


