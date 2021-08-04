from selenium import webdriver

import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 2080)") # 해상도 1920 x 1080

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 1 # 2초에 한번 씩 스크롤 내림

# 현재 문서 높이
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 가장 아래로 스크롤 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져옴
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height == prev_height:
        break

    prev_height = current_height

print("스크롤 완료")


soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

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

