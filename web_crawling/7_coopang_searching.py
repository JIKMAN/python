import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("")
        print("<광고상품 제외>")
        print("")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    if '델' in name:
        print("Dell 상품 제외")
        print("")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()
  
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("평점 없음")
        print("")
        continue

    review = item.find("span", attrs={"class":"rating-total-count"})
    if review:
        review = review.get_text()[1:-1]
    else:
        print("리뷰 없음")
        print("")
        continue
    # 평점 4.0 이상, 리뷰 100개 이상만 조회
    if float(rate) >= 4.0 and int(review) > 100:       
        print("제품명", name)
        print("가격", price)
        print("평점", rate)
        print("리뷰수", review)
        print("")
        

#     if float(rate) >= 4.0 and int(review) > 50:       
#         print("제품명", name)
#         print("가격", price)
#         print("평점", rate)
#         print("리뷰수", review)
#         print("")