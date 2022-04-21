"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req



# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
#print(res.read())

#받은 문서로 파싱하기
soup = BeautifulSoup(res,'html.parser')
result = soup.select('.market1 .head_info>.value')
#result = soup.select('div.head_info>span.value')
print('result:',result[0].text)#slect는 리스트로 가져오기 때문에 출력할때 인덱스 지정해줄것

result = soup.select_one('.market1 .head_info>.value')
print('result:',result.text)#slect는 리스트로 가져오기 때문에 출력할때 인덱스 지정해줄것


