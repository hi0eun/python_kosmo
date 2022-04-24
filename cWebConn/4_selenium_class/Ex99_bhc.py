"""#상세주소 빼고 주소 가져오기
address= ['서울 강서구 등촌동 707-1 상가107호']

# 주소 데이터 깔끔하게 다듬기
for i in range(len(address)):
    a = address[i].split(' ')
    address[i] = " ".join(a[0:4])
print(address)"""

#--------------------------------------------------------------------------
import time
from selenium import webdriver
from bs4 import BeautifulSoup
#-----------------위도경도를 위한 카카오API이용 import-------------------
import json
import requests
#----------------MariaDB import--------------------
import pymysql
#--------------------함수---------------------------
#주소를 위도경도로 변환
def addr_to_lat_lon(addr):
    try:
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
        headers = {"Authorization": "KakaoAK " + "55876398dc3bebef49e685b4806087bf"} #{,REST API 키}
        result = json.loads(str(requests.get(url, headers=headers).text))
        match_first = result['documents'][0]['address']
        return float(match_first['x']), float(match_first['y'])
    except:
        return ["위도출력불가","경도출력불가"]

#DB에 크롤링 값 넣기
config = {
     'host' : '127.0.0.1',
     'user' : 'scott',
     'password' : 'tiger',
     'database' : 'chicken',
     'port' : 3306,
     'charset':'utf8',
     'use_unicode' : True}

def set_db(name,tel,addr,latitude,longitude):
    #1. Connection 얻어오기
    conn = pymysql.connect(**config)
    # 2. sql 문장 만들기
    sql ='''
        INSERT INTO store (name,tel,addr,latitude,longitude)
        VALUES( "{0}", "{1}", "{2}", "{3}","{4}" )
        '''.format(name,tel,addr,latitude,longitude)
    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.commit()
    conn.close()

#-------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3) #크롬 드라이버 뜰때까지 기다려줘

driver.get('https://www.bhc.co.kr/location/search.asp')
time.sleep(3)
#사이트 이동할때 속도가 느림 이럴경우 우리와 시간이 다를경우 잘 안됨
#그래서 타이머 2~3초 넣어주기

for i in range(1, 169):

    driver.execute_script("goPage('{}')".format(i))
    #자바스크립트 실행하는 selenium함수
    #참고 블로그 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=shino1025&logNo=221305355357
    time.sleep(2)
    html = driver.page_source #페이지 주소를 html에 넣어줌
    # print((html))
    # [ 출력 ]
    soup = BeautifulSoup(html,'html.parser')
    #print(soup)

    store_list = soup.select('.register01 tr')

    for a in store_list:
        #print(a)
        try:
            name = a.select_one('td+td>div').text.strip() #.strip()데이터베이스 들어갈때 앞 뒤 공백 제거
        except:
            name = a.select_one('td+td a').text.strip()
        tel= a.select_one('td+td>p.mt10').text.split('\n')[2][7:].strip()
        addr= a.select_one('td+td>p.mt10').text.split('\n')[1][5:].strip()

        #주소 위도 경도로 변환
        address = addr_to_lat_lon(addr)
        set_db(name,tel,addr,address[0],address[1])
        print("가게이름:[{}] 전화번호:[{}] 주소:[{}] 위도:[{}] 경도:[{}] ".format(name,tel,addr,address[0],address[1]))



