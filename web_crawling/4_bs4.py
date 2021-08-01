import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.title.get_text()) # 타이틀
# print(soup.a) # soup 객체의 첫번째  element 출력
# print(soup.a.attrs) # a element의 속성 정보 출력
# print(soup.a["href"]) # a elemnet 의 href 속성 값 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class가 Nbtn_upload 인 a element를 찾기
'''Nbtn_upload가 유일한 클래스인 경우 print(soup.find(attrs={"class":"Nbtn_upload"}))와 같음'''

# print(soup.find("li", attrs={"class":"rank01"}).get_text())
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())

# rank2 = rank1.next_sibling.next_sibling # next_sibling 다음 태그로 넘어가는 커멘드
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent) # 부모태그

# rank2 = rank1.find_next_sibling("li") # li 테그를 기준으로 다음 테그를 찾음
# print(rank2.a.get_text())

# rank3 = rank2.find_previous_sibling("li") # li 테그를 기준으로 이전 테그를 찾음
# print(rank3.a.get_text())

# print(rank1.find_next_siblings("li"))

ranks = rank1.find_next_siblings("li")

for rank in ranks:
    print(rank.a.get_text())


# webtoon = soup.find("a", text="이번 생도 잘 부탁해-55화")
# print(webtoon)