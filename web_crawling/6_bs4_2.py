import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=736989&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 웹툰 제목, url 가져오기

webtoons = soup.find_all("td", attrs={"class":"title"})
for webtoon in webtoons:
    print(webtoon.get_text().split('\n')[1])
    print('https://comic.naver.com' + webtoon.a["href"], '\n')


# 웹툰 평점 구하기

webtoons = soup.find_all("div", attrs={"class":"rating_type"})
total_rates = 0

for wt in webtoons:
    rate = wt.strong.get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 :", total_rates)
print("평균 점수 :", total_rates / len(webtoons))