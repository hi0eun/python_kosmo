#Ex02_csv.py
#csv : common string value

import csv

'''data = [[1,'김','책임'],[2,'박','선임'],[3,'최','연구원']]

with open('./data/imsi.csv','wt',encoding='utf-8-sig') as f:
    count = csv.writer(f)
    count.writerows(data)'''

# csv 파일을 읽어서 리스트 변수에 저장

result = []

with open('./data/imsi.csv','rt',encoding='utf-8-sig') as f:
    cin = csv.reader(f)
    result = [n for n in cin if n]
    print(result)
