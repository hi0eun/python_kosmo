from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

config = {
     'host' : '127.0.0.1',
     'user' : 'scott',
     'password' : 'tiger',
     'database' : 'book',
     'port' : 3306,
     'charset':'utf8',
     'use_unicode' : True}

def set_db(img_link,title,author,publisher,date,price):
    #1. Connection 얻어오기
    conn = pymysql.connect(**config)
    # 2. sql 문장 만들기
    sql ='''
        INSERT INTO info (title,author,publisher,bdate,price)
        VALUES( "{0}", "{1}", "{2}", "{3}","{4}" )
        '''.format(img_link,title,author,publisher,date,price)
    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.commit()
    conn.close()



'''
html = urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=python')
soup = BeautifulSoup(html,'html.parser')

#책제목
datas = soup.select('#yesSchList > li > .itemUnit > .item_info > .info_row.info_name > a.gd_name')
#print(datas)
#책이미지정보
img_datas = soup.select('#yesSchList > li > div > div.item_img > div.img_canvas > span > span > a > em > img')
#print(img_datas)
#작가이름
authors = soup.select('#yesSchList > li > .itemUnit span.info_auth > a')
#출판사
publishers=soup.select('#yesSchList>li>div.itemUnit #spanGdKeynote>a')
#출판일
odate = soup.select('#yesSchList > li > .itemUnit span.info_date')
#가격
bprice = soup.select('#yesSchList > li > .itemUnit >.item_info>.info_price>.txt_num>em.yes_b')


import os
#os.mkdir('imgs')
os.makedirs('imgs', exist_ok=True )

for img, book_name, authorName,p_name,date,price in zip(img_datas, datas,authors,publishers,odate,bprice):
    #책이미지링크
    img_link = img['data-original']
    #책제목
    title = book_name.text.replace('/', ' ')
    #작가이름
    author = authorName.text
    #출판사
    publisher = p_name.text
    #출판일
    date = date.text
    #가격
    price = price.text

    print('이미지 : ',img_link,
          '책 제목 :', title,
          '작가 : ',author,
          '출판사 : ',publisher,
          '출판일 : ',date,
          '가격 : ',price)
    set_db(img_link,title,author,publisher,date,price)

    #책 이미지 저장하기
    request.urlretrieve(img_link, './imgs/{}.png'.format(title))
'''
#--------------------------------------------------------------------------------------
html = urlopen("http://www.yes24.com/Product/Search?domain=ALL&query=python")

soup = BeautifulSoup(html,'html.parser')
#print(soup)

#책제목 가져오기
titles = soup.select('.itemUnit .gd_name')
# for title in titles:
#     print("책 제목:",title.text)
# print(len(titles),'권')

#이미지 가져오기
#내가만든 거
img = soup.select('.itemUnit .img_bdr>img')
#작가이름
authors = soup.select('#yesSchList > li > .itemUnit span.info_auth > a')
#출판사
publishers=soup.select('#yesSchList>li>div.itemUnit #spanGdKeynote>a')
#출판일
odate = soup.select('#yesSchList > li > .itemUnit span.info_date')
#가격
bprice = soup.select('#yesSchList > li > .itemUnit >.item_info>.info_price>.txt_num>em.yes_b')

import os
#os.mkdir('imgs')
os.makedirs('imgs', exist_ok=True )

for imgadr, book_name, authorName,p_name,date,price in zip(img, titles ,authors,publishers,odate,bprice):
    #print(imgadr.attrs['src'])
    url=imgadr.attrs['data-original']
    title = book_name.text.replace('/', ' ')
    print('이미지 : ', url,
          '책 제목 :', title,
          '작가 : ', authorName.text,
          '출판사 : ', p_name.text,
          '출판일 : ', date.text,
          '가격 : ', price.text)
    set_db(url, title, authorName.text, p_name.text, date.text, price.text)

    # 책 이미지 저장하기
    request.urlretrieve(url, './imgs/{}.png'.format(title))


