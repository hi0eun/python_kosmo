from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

# http://www.pythonscraping.com/pages/warandpeace.html
# 녹색 글자만 추출하여 출력

# 웹 문서 가져오기
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

# 1. 데이타 파서하기
soup = BeautifulSoup(html, 'html.parser')

# 2. 원하는 요소 접근하기
#h = soup.html.body.ul.li.a
data =soup.select('.green')

for green in data:
    print(''.join(green.text.split()))

# http://www.pythonscraping.com/pages/page3.html
# 아이템과 가격을 추출

html_ex2 = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_ex2 = BeautifulSoup(html_ex2, 'html.parser')
title_ex2 = soup_ex2.select('.gift > td:nth-child(1)')
cost_ex2 = soup_ex2.select('.gift > td:nth-child(3)')
for t, c in zip(title_ex2, cost_ex2):
    print('{title}의 가격은 {cost}입니다.'.format(title=t.text.replace('\n', ''), cost=c.text.replace('\n', '')))

# https://wikidocs.net/
#  1) 책 제목과 저자만 추출
#  2) 이미지 다운
from urllib import parse
import urllib
import os
os.makedirs('img', exist_ok=True )

baseUrl = 'https://wikidocs.net/'

html_ex3 = urlopen("https://wikidocs.net/")
soup_ex3 = BeautifulSoup(html_ex3, 'html.parser')
title_ex3 = soup_ex3.select('.media .media-heading>.book-subject')
author_ex3 = soup_ex3.select('.media .book-detail .menu_link')
imgs_ex3 = soup_ex3.select('.media .book-image-box>.book-image')

try:
    for t, a ,i in zip(title_ex3, author_ex3, imgs_ex3):
        print('{title}의 저자는 {author}입니다.'.format(title=t.text.replace('\n', ''), author=a.text.replace('\n', '')))
        img_link = parse.urljoin(baseUrl, '{}'.format(urllib.parse.quote(i.attrs['src']))) #urllib.parse.quote() => 한글처리
        request.urlretrieve(img_link, './img/{}.png'.format(t.text.replace(':','')))
except:
    print('예외발생')
