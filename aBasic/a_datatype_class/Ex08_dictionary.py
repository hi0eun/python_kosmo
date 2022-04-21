"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one',
      2:'two',
      '3':'three',
      1 : 'hana',
      3 : 'sam'} 
# 키가 중복되는 경우 덮어쓰기 됨
# 키는 자료형까지 따짐으로 3과 '3'은 다름

print(dt)
print(dt[1]) # dt[key] dt의 key 1의 값만 추출
print(dt['3']) # 키의 자료형까지 맞춰줘야함

# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}


print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
# 값 추가 : 딕셔너리(dictionary)명[존재하지않은  key명] = value
# 값 수정 : 딕셔너리(dictionary)명[존재하는 key명] = value => 덮어쓰기 됨
dt['korea'] = 'seoul'
print(dt)
dt['korea'] = '서울'
print(dt)

# 여러개 추가할 때
# update함수사용
dtemp = { 4 : 'kim', 5 : 'OH'}
dt.update(dtemp)
print(dt)

print('--------- 3. Key로 Value값 찾기  --------------- ')
# print(dt[9]) #에러발생
print(dt.get(9)) #None => dt의 key에 9가 없다는 뜻
print(dt.get(9,'없음')) #None =-> 없음






# Key와 Value만 따로 검색
print(dt.keys()) #key만 추출 (임의의 순서)
print(dt.values()) # value만 추출 (임의의 순서)
print(dt.items()) #key와 value를 튜플로 추출 (임의의 순서)