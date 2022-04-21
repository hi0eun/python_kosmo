from urllib import request #request에 s가 붙지 않음
#urllib은 파이썬 자체의 내장모듈이라 install안해도됨
#requests는 외장 모듈

site = request.urlopen('http://www.google.com')
#requests는 get방식과 post방식등으로 사용 하는데 request는 urlopen사용
print(site)
print('-'*50)
print(site.status)
#requests은 바로 상태값을 알려주지만 request는 안알려주기때문에 알고싶다면 .status이용해야함

#requests.content와 같이 그 페이지의 내용 가져오는 법
page = site.read()
print(page)

#해당하는 사이트가 없다면 try 해야함
