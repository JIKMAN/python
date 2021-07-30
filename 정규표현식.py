import re

p = re.compile('[a-z]+')
m = p.match('python')
print(m)
# 일치하면 리턴해주고, 일치 안하면 None

n = p.search('3 python')
print(n)
# 일치하는 부분만 리턴해줌

f = p.findall('life is too short')
print(f)
# 일치하는 문자열을 찾아 리스트로 나눔

i = p.finditer('life is too short')
for r in i:
    print(r)
# 일치하는 문자열을 각각의 객체로 리턴함

'''매치 된 객체에 사용할 수 있는 명령어'''
print(m.group()) # 매치된 문자열
print(m.start()) # 매치된 문자열의 첫 인덱스
print(m.end()) # 매치된 문자열 끝 인덱스
print(m.span()) # 매치된 문자열 시작부터 끝 인덱스 범위 리턴