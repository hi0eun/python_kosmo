"""
    BeautifulSoup 모듈에서
    - HTML의 구조(=트리구조)에서 요소를 검색할 때 : find() / find_all()
    - CSS 선택자 검색할 때 : select() -> 값 리스트로 가져옴 /  select_one()
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""

# 1. 데이타 파서하기
soup = BeautifulSoup(html, 'html.parser')

# 2. 원하는 요소 접근하기
#h = soup.html.body.ul.li.a
div1=soup.select_one('#course > h1').text
print(div1)

div2=soup.select('#subjects > .subs li')
for t in div2:
    print(t.text)




'''for a in h:
    print("{name} : {adr}".format(name=a.text,adr=a.attrs['href']))'''