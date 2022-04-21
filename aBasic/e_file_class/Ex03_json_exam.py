#Ex03_json_exam.py

#data / sample.json 읽어서 총합을 구해서 출력

import json

f = open('./data/sample.json','rt',encoding='utf-8')
data = f.read()
items = json.loads(data)


print('-'*50)
sum_price = 0
sum_cnt = 0
for s in items.values():
    sum_price += s['price']
    sum_cnt += s['count']

print('총 합은',sum_price , '총 개수는' , sum_cnt)

print('-'*50)
sum_price = sum(s['price'] for s in items.values())
sum_cnt = sum(s['count'] for s in items.values())

print("총 합은 {}, 총 개수는 {}".format(sum_price,sum_cnt))
