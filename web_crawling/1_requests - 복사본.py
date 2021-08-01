import requests

res = requests.get("http://www.google.com")
# res.status_code > 200이면 정상작동
res.raise_for_status() # 스크롤링 가능한 페이지면 계속진행, 아니면 오류남

print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)