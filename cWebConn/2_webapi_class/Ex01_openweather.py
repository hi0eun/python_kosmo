"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""

# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
import json

apikey = "1db47184ebbc18af53fd996be840d270"

# 날씨를 확인할 도시 지정하기
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

# url 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k - 273.15 #lambda는 3버전이후 쓰는걸 권장하지않음
'''
    def k2c(k)
        return k - 273.15
'''

import requests

for city in cities:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}".format(city=city,key=apikey))

    #print(res.text)
    #json형태의 문자열 단순 문자임 아직 객체로 안올라와았기때문에 딕셔너리 아님 메모리에 안올라왔기 때문

    data = json.loads(res.text)
    #메모리에 객체로 올리기 딕셔너리로 만들기
    #딕셔너리라 문자를 원하는대로 가져올 수 있음
    #print(data)
    print('도시명:', data['name'])
    print('최저기온:',data['main']['temp_min'])
    print('최고기온:',data['main']['temp_max'])
    print('습도:',data['main']['humidity'])
    print('기압:',data['main']['pressure'])
    print('풍속:',data['wind']['speed'])
    print('-'*30)