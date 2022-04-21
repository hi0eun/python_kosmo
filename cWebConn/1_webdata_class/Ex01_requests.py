"""
    파이썬에서 웹을 요청할 수 있는 라이브러리
        1- requests 라이브러리 (s붙음 주의) - 추가
        2- urllib 라이브러리 - 내장모듈
            `request
    차이점
        1- requests는 요청 메소드(get/post)를 구분하지만 urllib는 보내는 데이타 여부에 따라 구분됨
        2- 데이타 보낼 때 requests는 딕셔러니 형태로 urllib는 인코딩한 바이너리 형태로 보낸다
        
    requests 라이브러리 추가
    메뉴 > File > Settings > Project Interpreter > + 버튼 > 'requests' 검색 후 인스톨

[ requests 모듈 ]
(1) Rest API 지원
    import requests
    resp = requests.get('http://www.mywebsite.com/user')
    resp = requests.post('http://www.mywebsite.com/user')
    resp = requests.put('http://www.mywebsite.com/user/put')
    resp = requests.delete('http://www.mywebsite.com/user/delete')

(2) 파라미터가 딕셔너리 인수로 가능
    data = {'firstname':'John', 'lastname':'Kim', 'job':'baksu'}
    resp = requests.post('http://www.mywebsite.com/user', data=userdata)

(3) json 디코더 내장 (따로 json 모듈 사용 안해도 됨)
    resp.json()
"""

import requests #외장모듈
'''
url = 'http://www.google.com'
res = requests.get(url)
print(res) #<Response [200]>

200 갔다가왔는데 문제없이 성공함
405 접근 불가
500 서버문제 
'''
# res=requests.post(url) #post방식은 폼에서만 이용할수 있기 때문에 오류
# print(res) #<Response [405]>

url = 'http://www.google.com'
res = requests.get(url)
print(res.text)
print('-'*50)
print(res.content)
#출력에 b가 붙었음 파이썬은 기본적으로 문자형태를 utf-8로 읽는데
#b를 붙은건 바이트어레이 형태로 저장할거라는 신호를 준 것
#여러 글자들이 붙음 정리해둘 것
print('-'*50)
print(res.headers)
#넘어오는 구조 모양이 딕셔너리
for k,v in res.headers.items() :
    print('key:',k, '////',"value:",v)