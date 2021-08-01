import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
''' User Agent란 유저마다 가진 웹 브라우저와 OS정보를 담고 있는 개념이다.
웹 서버에서 각각의 User Agent를 decode 하여 화면을 보여주게 된다.'''
url = "https://github.com/JIKMAN"

res = requests.get(url, headers=headers)
res.raise_for_status()

with open("coding.html", "w", encoding="utf8") as f:
    f.write(res.text)