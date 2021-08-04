from selenium import webdriver

import requests
from bs4 import BeautifulSoup

# 백그라운드로 크롬 띄우기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 1 # 2초에 한번 씩 스크롤 내림

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    current_height = browser.execute_script("return document.body.scrollHeight")
    
    if current_height == prev_height:
        break

    prev_height = current_height

print("스크롤 완료")
# 백그라운드에서 돌던 화면 스크린샷 저장
browser.get_screenshot_as_file("google_movie.png")


soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격 정보
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue

    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    # 링크 정보
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("*" * 100)