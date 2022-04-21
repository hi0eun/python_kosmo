"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""


def func():
    print('inside func')

func()
result = func()
print('result =', result) #리턴값이 없으면 None



def func():
    print('inside func')
    return 'hello'

func()
result = func()
print('result =', result)

#(2)리턴값이 여러개인 경우
def func(arg):
    return arg + 5, arg -5

add, minus = func(10)
print('add =',add)
print('minus =',minus)


#(3) 위치 인자 (positional argument)
def func(greeting,name):
    print( greeting, '!!!!!' , name, '님')

func("안녕하세요","홍길동")
func("마이클","하이")

#(4) 키워드 인자 (keyword argument)
func(name="마이클2",greeting="하이2")

#매개변수 지정(기본값 지정)
def func(greeting, name='아무개'):
    print(greeting,'!!!!', name, '님')
func("안녕하세요","홍길동")
func("올라") #매개변수 개수가 맞지않으면 오류남 그래서 기본값 지정해줘야함

#[참고]
def func(a,b,c=100):
    return a*2 + b*3 + c*4

print(func(c=1, b=2, a=3)) #6+6+4=16
print(func(1,2,3)) #2+6+12=20
print(func(1,2)) #2+6+400 = 408





'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

'''
def func(a,b,c=0, *args):
    sum = a+b+c
    for i in args:
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다


#(6) 키워드 인자 모으기
def func(a,b,c=0, *args, **kwargs):
    sum = a+b+c
    for i in args:
        sum += i
    for j in kwargs:
        sum += kwargs[j]
        print("키값은 ", kwargs[j])
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
print(func(4, 5, 6, 7, kor=80,eng=70)) #딕셔너리로 넘어감 {key,value}
print(func(4, 5, 6, 7, kor=80,eng=70,java=60))

