"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25        = 21
            - 16진수  0x25        = 256 + 80 = 336
"""

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : alt + shift + F10

""" [ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승 (n제곱)
    
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        is      : 비교하는 객체의 주소가 같으면 true, 다르면 false
        is not  : 비교하는 객체의 주소가 다르면 true, 같으면 false 
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
      

    [참고] 증가(++), 감소(--) 연산자 없음         
"""

a = 5
b = 2

#str = 'hello'
#*********************************변수명으로 str 사용하지 맙시다.


add = a + b
#print('a + b =' + add)
print('a + b = ' + str(add)) #자바식
print('a + b = ',add) # 파이썬식
""" 파이썬은 문자 + 숫자 안됨 """

""" [ 출력결과 ] 
        a + b = 7
        a - b = 3
        a * b = 10
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25 => a의 b 제곱
"""

# 기타연산자
print("Hello" == "hello") #False
print("Hello" != "Hello") #False
print('H' in 'Hello') #True
print('H' not in 'Hello') #False

# 출력 포맷
# c, java언어 : printf()

y=8.4/5.3
print(y)

print(' 실수 : {0:.2f}'.format(y)) #반올림 됨
print(' 실수 : {0}, 정수 {1}  '.format(y, 8.4//5.3))
print(' 실수 : {}, 정수 {}  '.format(y, 8.4//5.3))
print(' 실수 : {1}, 정수 {0}  '.format(y, 8.4//5.3))

a=3.5
b=(int(3.5))
print(a-b)
print((a-b)*a)
print(1.75%3)
b=(((a-b)*a)%b)
print(b)


