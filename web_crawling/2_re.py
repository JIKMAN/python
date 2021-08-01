import re

p = re.compile("ca.e") 
# # . (ca.f): 하나의 문자를 의미 > cafe, care ...
# # ^ (^de): 문자열의 시작 > desk, destination ...
# # $ (se$): 문자열의 끝 > case, base ...

def print_match(m):
# 매치되지 않으면 에러가 발생
    if m:
        print("일치하는 문자열:", m.group())
        print("입력받은 문자열:", m.string)
        print("일치문자열 시작인덱스:", m.start())
        print("일치문자열 끝 인덱스:", m.end())
        print("시작과 끝 인덱스:", m.span())
        print("")
    else:
        print("매칭되지 안음")

m = p.match("cafe") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

n = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(n)

lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로
print(lst)