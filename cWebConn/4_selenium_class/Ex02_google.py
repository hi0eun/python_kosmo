'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

# [1]
from selenium import webdriver
# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2) #창 뜨기전에 2초정도 기다려줘라
# 2. 페이지 접근
driver.get('https://www.google.com')

#구글 검새창에 코로나극복치고 검색하게하기
search_bt = driver.find_element_by_name('q') #name으로 요소를 찾겠다 크롬의 검색창 name이 'q'임
search_bt.send_keys('코로나극복')
search_bt.submit()
#홈태그에서 input태그 하나만 있으면 그게 submit역할을 함
#구글은 메인페이지에 input태그 하나만 둠


