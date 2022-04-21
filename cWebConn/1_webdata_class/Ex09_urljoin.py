"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""
from urllib import parse

baseUrl = 'http://www.example.com/html/a.html'

print(parse.urljoin(baseUrl,'b.html')) #파일을 바꿈

print(parse.urljoin(baseUrl,'sub/c.html')) #상대경로 파일의 폴더를 만듬
print(parse.urljoin(baseUrl,'/sub/c.html')) #절대경로

print(parse.urljoin(baseUrl,'../sub/d.html')) #부모한테 올라갔다가 /sub로 내려오고
print(parse.urljoin(baseUrl,'../temp/d.html')) #부모한테 올라갔다가 없는 /temp로 내려올거임

print(parse.urljoin(baseUrl,'http://www.other.com')) #다른 링크로 덮어쓰기 됨
print(parse.urljoin(baseUrl,'www.other.com'))

