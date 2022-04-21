#Ex03_json.py

import json

f = open('./data/temp.json','rt',encoding='utf-8')

data = f.read()
#단순글자로 처리하기
print(data)

#json으로 처리하기
print('-'*100)
items = json.loads(data)
print(items)
print('-'*100)

print(type(data))
print(type(items)) #딕셔너리로 데이터를 올려서 key,value형식으로 나옴 활용 가능

#딕셔너리 활용
for k,v in items.items():
    print(k ,':', v, '>>' , v['Job'])

#json으로 처리할 시 딕셔너리로 출력되기 때문에 데이터 분석이 원할해짐