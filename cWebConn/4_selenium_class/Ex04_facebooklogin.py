"""
    [연습] 페이스북에 접속해서 로그인 하기

        로그인 후에 보안창은 없는데 안 넘어가서

        from selenium.webdriver.common.keys import Keys

        아이디와 패스워드 지정후에
        elem.send_keys(Keys.RETURN)

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 0. 페이스북 로그인 정보
myID = '아이디'
myPW = '비밀번호'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2) #창 뜨기전에 2초정도 기다려줘라
# 2. 페이지 접근
driver.get('https://www.facebook.com/')

#3. 네이버로그인페이지의 입력하는 곳과 버튼 가져와서 입력값넣기
driver.find_element_by_name('email').send_keys(myID)#name이 id인거에 내가 지정한 myID입력하겠다
driver.find_element_by_name('pass').send_keys(myPW)

driver.find_element_by_name('login').click() #버튼을 클랙하게하는 것