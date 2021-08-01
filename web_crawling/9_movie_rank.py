import requests
from bs4 import BeautifulSoup
from requests.api import request

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

for year in range(2017, 2021):

    url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={year}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84"

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("div", attrs={"class":"thumb"})


    for i, image in enumerate(images):
        print(i+1)
        img_url = image.find("img")['src']

        img_res = requests.get(img_url)
        img_res.raise_for_status()

        
        if i < 5:
            with open(f"./naver_movies/movie-{year}-{i+1}.jpg", "wb") as f:
                f.write(img_res.content)
        else:
            break