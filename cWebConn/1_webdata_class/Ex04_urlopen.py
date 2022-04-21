
# urlretrieve(): 파일로 바로 저장
# urlopen(): 파일로 바로 저장하기 않고 메모리에 로딩을 한다.

""" [참고] 파일저장 기본방식
    f = open('a.txt','w')
    f.write("테스트 내용")
    f.close()

    위의 과정을 with 문으로 간략하게 close 필요없음
    with open("a.txt","w") as f:
        f.write("테스트 내용")
"""

#Ex03_retretrieve.py 와 결과는 같고 방식이 다를 뿐 둘다 알아놓을 것

from urllib import request

url='https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png'
imgName = 'data/daum.png'

site = request.urlopen(url) #웹사이트 오픈
page = site.read()

with open(imgName,'wb') as f : #파일오픈 / 'wb'는 쓰고(w) 이미지(바이너리)
    f.write(page)

url = 'https://image.yes24.com/goods/74419916/L'