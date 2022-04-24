#Ex01_test.py
#크롬으로 네이버 들어가서 그 화면 캡쳐하기

"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""
from selenium import webdriver
# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')

# 2. 페이지 접근
driver.get('https://www.naver.com')

# 3. 화면을 캡처해서 저장하기
driver.save_screenshot('MyShot.png')

#여기까지 다 되면 접속가능하다는 것과 selenum과 웹드라이버 버전이 잘 맞았다는 뜻임