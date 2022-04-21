"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + ctrl + F10

    [도움말] ctrl + q

"""

""" 여러줄 주석 """
# 한줄 주석

# 문자열표시
print("헬로우")
print('hello')
print("""안
녕""")
print('''올
라''')
# 실행 : shift + ctrl + F10
# """과 '''는 공백과 줄바꿈도 가능함

'''
변수란
    파이션의 모든 자료형은 객체로 취급한다 ( 전부 다 참조형 ) 
    a = 7
            7 객체을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
    
    [ 파이썬의 자료형 ]
    1.기본형
        -숫자형
        -문자형
        -논리형
        -날짜형
    
    2.집합형
        -list
        -set
        -dictionary
        -tuple
'''

import  keyword
print(keyword.kwlist)
# 파이썬에서 False,None,True는 첫 글자가 대문자

a = 7
b = 7
print(id(7))
print(id(a))
print(id(b))
#주소값이 동일함
#7이라는 객체를 a와 b가 가르킴

print( a == 7)
print( a == b )

a = 777
b = 777
print(id(a))
print(id(b))
print( a == b )
# 파이썬 3.8이하는 False나옴 
# 256까지만 파이썬이 미리 데이터에 올려놓고 그 이후는 데이터가 그때 그때 올라감



class Person(object):
    def __init__(self, name):
        self.name = name
    def language(self):
        pass

class Earthling(Person):
    def language(self, language):
        return language

class Groot(Person):
    def language(self, language):
        return "I'm Groot!"
name = ['Gachon', 'Dr.Strange', 'Groot']
country = ['Korea', 'USA', 'Galaxy']
language = ['Korean', 'English', 'Groot']
for idx, name in enumerate(name):
    if country[idx].upper() != 'GALAXY':
        person = Earthling(name)
        print(person.language(language[idx]))
    else:
        groot = Groot(name)
        print(groot.language(language[idx]))