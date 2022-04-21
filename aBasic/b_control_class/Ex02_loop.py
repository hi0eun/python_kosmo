
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다. e는 key만 뽑아져나옴
    print(entry , ':', e[entry])

for entry in e.items():
    print(entry) #결과가 튜플로 나옴

for k,v in e.items(): #튜플은 집합이기 때문에 분해가 가능해서 k에는 key를 v에는 value를 자동으로 넣어줌
    print(k, "," , v)

#--------------------------------
a = ['z','y','x']

while a:
    data = a.pop() # 마지막꺼 뽑아냄
    print(data)
else : print("끝")




"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
#구구단 만들기
for i in range(2,10):
    for j in range(1,10):
        print ('{0} * {1} = {2}'.format(i, j, i*j))
    print('---'*10)


alist = ["a", "1", "c"]

blist = ["b", "2", "d"]


for a, b in enumerate(zip(alist, blist)):
    print(a)
    print(b)