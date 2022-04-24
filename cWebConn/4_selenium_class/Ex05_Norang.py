"""
    [ 노랑통닭 매장 주소 가져오기 ]

    노랑통닭 http://www.norangtongdak.co.kr/ > 매장찾기 > 매장찾기
                  http://www.norangtongdak.co.kr/store/store.html

    개발자모드( F12 ) 열고 페이지 번호를 누르면 링크 확인

"""
import time

from selenium import webdriver

#-------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3) #크롬 드라이버 뜰때까지 기다려줘
from bs4 import BeautifulSoup

norang_list = []
for i in range(1, 11):  #1부터 10페이지까지 돌리겠다
    # 페이지 접근
    driver.get('http://www.norangtongdak.co.kr/store/store.html?p=%d' % i)
    time.sleep(3)
    #노랑통닭 사이트가 사이트 이동할때 속도가 느림 이럴경우 우리와 시간이 다를경우 잘 안됨
    #그래서 타이머 2~3초 넣어주기
    html = driver.page_source
    #print((html))

    # [ 출력결과 ] 매장명-전화번호-주소

    soup = BeautifulSoup(html,'html.parser')
    stor_list = soup.select('#new_wrap>div')
    #print(stor_list)
    name = soup.select('#new_wrap>div>div>p.txt1')
    adr = soup.select('#new_wrap>div>div li.txt2')
    tel = soup.select('#new_wrap>div>div li.txt3')

    for n, a, t in zip(name,adr,tel):
        norang_list.append([n.text,'-',a.text,'-',t.text])
print(norang_list)