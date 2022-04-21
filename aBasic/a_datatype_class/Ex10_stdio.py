"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

name = input('이름을 입력하세요')
print('당신의 이름은 ', name ,'입니다')

#format()이용
print('당신의 이름은 {name}입니다'.format(name=name))

#%이용
print('당신의 이름은 %s입니다' %name)

#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
age = eval(input('나이를 입력하세요')) + 1
print('당신의 나이는 ', age,'입니다')

#다른 분이 한 것
age = input('나이를 입력하세요')
print('당신의 나이는 ', eval(age)+1,'입니다')

height=input('키를 입력하세요')
print('당신의 키는', float(height),'입니다')
#실수형인지 정수형인지 모를때는 eval함수 쓰지만
#받으려는 값이 정확하면 int(),float(),str()같이 명확히 지정해주는게 좋음

print('1+2')
print(eval('1+2'))

# 파이썬에서 가능 한 것들 셋 중에 편한거 쓰면 됨
print('친구' + '안녕')
print('친구','안녕') #,는 한칸 떨어짐
print('친구' '안녕')

#파이썬의 for문
for i in range(1, 5, 2): #range(시작점, 끝 , 건너뛰기)
    print(i) #개행함

for i in range(5):
    print(i , end =',' if i < 4 else '')
    #i가 4보다 작으면 ,찍고 4보다 크면 '' => 1,2,3,4,가 아니라 1,2,3,4
    #print(i, end= '')개행 안함  print(i , end = ',' ) 요소마다,찍힘

#----------------------------------
# 단을 입력받아 구구단을 구하기
print()
x=int(input('몇 단을 출력할까요?'))
print("------- [" + str(x) + "단] -------")
for y in range(1, 10):
    print(x, "X", y, "=", x*y)


#-----------------------------------------
# print() 함수



# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
