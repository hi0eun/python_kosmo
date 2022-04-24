"""
[1]넷플릭스
[2]인스타그램
[3]다음
[4]네이버
[5]다음 카카오로그인

"""

"""
#[1]----------------------------------------------------------------------------------------------------
from selenium import webdriver


# 0.로그인 정보
myID = '본인의 아이디'
myPW = '비밀번호'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2) #창 뜨기전에 2초정도 기다려줘라
# 2. 페이지 접근
driver.get('https://www.netflix.com/kr/login')

#3. 네이버로그인페이지의 입력하는 곳과 버튼 가져와서 입력값넣기
driver.find_element_by_name('userLoginId').send_keys(myID)#name이 id인거에 내가 지정한 myID입력하겠다
driver.find_element_by_name('password').send_keys(myPW)

driver.find_element_by_class_name('login-button').click() #버튼을 클랙하게하는 것

#[2]----------------------------------------------------------------------------------------------------

# 0. 인스타 로그인 정보
myID = ''
myPW = '비밀번호'
login_option = "instagram"
login_btn = '.sqdOP.L3NKy.y3zKF'
# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2)
# 2. 페이지 접근
driver.get('https://www.instagram.com/')
# 3. 조작
driver.find_element_by_name('username').send_keys(myID)
driver.find_element_by_name('password').send_keys(myPW)
login_btn_ok = driver.find_element_by_css_selector(login_btn)
login_btn_ok.click()

#[3]----------------------------------------------------------------------------------------------------

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
# 2. 페이지 접근
driver.get('https://logins.daum.net/accounts/signinform.do')
driver.find_element_by_name('id').send_keys(myID)
driver.find_element_by_name('pw').send_keys(myPW)
driver.find_element_by_id('loginBtn').click()


#[4]----------------------------------------------------------------------------------------------------
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip #pip install pyperclip
import time

browser = webdriver.Chrome('webdriver/chromedriver.exe')
# 현재파일과 동일한 경로일 경우 생략 가능
user_id = 'naver_id'
user_pw = 'naver_pw'
# 1. 네이버 이동
browser.get('https://nid.naver.com/nidlogin.login')
# 2. id 복사 붙여넣기
elem_id = browser.find_element_by_id('id')
elem_id.click()
pyperclip.copy(user_id)
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# 3. pw 복사 붙여넣기
elem_pw = browser.find_element_by_id('pw')
elem_pw.click()
pyperclip.copy(user_pw)
elem_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# 5. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()
"""

#[5]----------------------------------------------------------------------------------------------------
from selenium import webdriver

driver = webdriver.Chrome('./webdriver/chromedriver.exe')

url = "https://www.daum.net"
driver.get(url)

driver.find_element_by_xpath('//*[@id="inner_login"]/a[1]').click()
#driver.find_element_by_css_selector("link_login").click()

user_id = "lovel0113@naver.com"
user_passwd = "ae6694ae!!"
driver.find_element_by_id('id_email_2').send_keys(user_id)
driver.find_element_by_id('id_password_3').send_keys(user_passwd)

driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
#driver.find_element_by_css_selector("btn_g").click()
