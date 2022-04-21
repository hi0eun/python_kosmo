'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''

from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")'''


'''
html = urlopen("http://www.yes24.com/Product/Search?domain=ALL&query=python")

soup = BeautifulSoup(html,'html.parser')
#print(soup)

#책제목 가져오기
titles = soup.select('.itemUnit .gd_name')
for title in titles:
    print("책 제목:",title.text)
print(len(titles),'권')


#이미지 가져오기
#내가만든 거
img = soup.select('.itemUnit .img_bdr>img')
for imgadr in img:
    #print(imgadr.attrs['src'])
    url=imgadr.attrs['data-original']
    imgName = 'imgs/{imgName}.png'.format(imgName=imgadr.attrs['alt'].replace('/',' '))
    print(url,'////',imgName)
    site = request.urlopen(url)
    page = site.read()

    with open('{}'.format(imgName), 'wb') as f:
        f.write(page)'''

#다른분 + 선생님
# 교보문고 > '파이썬' 검색 > 국내도서
# html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")

html = urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=python')
soup = BeautifulSoup(html,'html.parser')

datas = soup.select('#yesSchList > li > .itemUnit > .item_info > .info_row.info_name > a.gd_name')
print(datas)
img_datas = soup.select('#yesSchList > li > div > div.item_img > div.img_canvas > span > span > a > em > img')
print(img_datas)

import os
#os.mkdir('imgs')
os.makedirs('imgs', exist_ok=True )
count=0
for img, book_name in zip(img_datas, datas):
    img_link = img['data-original']
    title = book_name.text.replace('/', ' ')
    print(img_link, title)
    count+=1
    # page = urlopen(img_link).read()
    # with open('data/' + title+'.png', 'wb') as f:
    #     f.write(page)
    request.urlretrieve(img_link, './imgs/{}.png'.format(title))
print("총",count,'권')