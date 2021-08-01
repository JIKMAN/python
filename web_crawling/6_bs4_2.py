import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=736989&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

webtoons = soup.find_all("td", attrs={"class":"title"})
for webtoon in webtoons:
    print(webtoon.get_text().split('\n')[1])
    print('https://comic.naver.com' + webtoon.a["href"], '\n')