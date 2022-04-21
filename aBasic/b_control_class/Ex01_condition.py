"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값 (0과 공백)
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

a = -1
if a :
    print('True') #
else :
    print('False')

if not a :
    print('True2') # a가 True임으로 not a는 False 그래서 수행되지않음

#-----------------------------------------------
a = 10
b = -1

if a and b: #and는 둘다 True여야만 True a도 True b도 True임으로 True3
    print('True3')
if a or b : #or은 둘 중에 하나만 True면 됨
    print('True4')

print(a and b) #a가 True여도 and 뒤의 b가 결론내기 때문에 -1나옴
print(a or b)  #a가 True면 or은 무조건 하나만 True여도 True이기 때문에 a가 True임으로 결정적인 애임으로 10나옴
#True False를 결정시키는 값으로 나옴

a = 0

if a:
    print('A')

print('B')
print('C')

#------------------------------------------------
a = 10
b = -1

if a :
    c = 2
elif b:
    c = 4
else:
    c = 6
print(c)
#지역변수 글로벌변수 개념이 없음



