"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = '본인의 네이버아이디'
myPW = '비밀번호'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2) #창 뜨기전에 2초정도 기다려줘라
# 2. 페이지 접근
driver.get('https://nid.naver.com/nidlogin.login')

#3. 네이버로그인페이지의 입력하는 곳과 버튼 가져와서 입력값넣기
driver.find_element_by_name('id').send_keys(myID)#name이 id인거에 내가 지정한 myID입력하겠다
driver.find_element_by_name('pw').send_keys(myPW)

driver.find_element_by_id('log.login').click() #버튼을 클랙하게하는 것






