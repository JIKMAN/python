import requests
import re
from bs4 import BeautifulSoup


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}

for i in range(1,6):
    print("-"*46, f"페이지{i}" + "-"*46, "\n")
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=&backgroundColor="
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("")
            print("<광고상품 제외>")
            print("")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        if '델' in name:
            print("Dell 상품 제외")
            print("-"*100)
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

        link = item.find("a", attrs={"class":{"search-product-link"}})["href"]

        # 평점 4.0 이상, 리뷰 100개 이상만 조회
        if float(rate) >= 4.0 and int(review) > 100:       
            print("제품명", name.split(",")[0])
            print("가격", price)
            print("평점", rate)
            print("리뷰수", review)
            print(f"https://www.coupang.com{link}")
            print("-"*100)











# for i in range(1,6):
#     print("현재 페이지 :", i)
#     url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=4&backgroundColor="

#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#     items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

#     for item in items:

#         ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
#         if ad_badge:
#             print("<광고상품 제외>")
#             print("")
#             continue

#         name = item.find("div", attrs={"class":"name"})
#         name = name.get_text().split(",")[0]
#         price = item.find("strong", attrs={"class":"price-value"})
#         price = price.get_text()
    
#         rate = item.find("em", attrs={"class":"rating"})
#         if rate:
#             rate = rate.get_text()
#         else:
#             rate = "평점 없음"

#         review = item.find("span", attrs={"class":"rating-total-count"})
#         review = review.get_text()[1:-1]

#         link = "https://www.coupang.com" + item.a["href"]

#         if float(rate) >= 4.0 and int(review) > 50:       
#             print(f"제품명 : {name}")
#             print(f"가격 : {price}")
#             print(f"평점{rate}")
#             print(f"리뷰수{review}")
#             print(link)
#             print("")