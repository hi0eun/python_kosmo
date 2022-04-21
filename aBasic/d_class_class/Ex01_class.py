"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""



'''[ 자바인 경우 ]
class Sample {
    String data = "Hello";
    String name;
    public Sample(){ #생성자 함수 void도 없어야함 
        this.name = name;
    }
}
'''

class Sample:
    data = 'Hello'
    def __init__(self, name, age):
        self.name = name #멤버변수 /self = 자바에서 this
        self.age = age  #멤버변수
        print('객체 생성')

    def __del__(self):
        print('객체 소멸되기 직전에 불려지는 함수')

s = Sample("홍길동",25)
print(s.data)
print(s.name)
print(dir(s))
del s # 소멸자 , 객체를 소멸 시킴  자바를 제외하고는 c언어나 파이썬은 객체를 해제해줘야함









"""
    1) 인스턴스와 클래스 변수
        클래스 변수 : 클래스명.변수 #자바의 static과 같음 : 부르기 전에 메모리에 올려두는것 /파이썬에서는 스텍틱이라는 용어는 쓰지말것 
        인스턴스 변수 : 인스턴스명.변수
    
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
"""

class Book:
    cnt = 0
    def __init__(self,title):
        self.title = title
        self.cnt += 1

    def output(self):
        print(self.title)
        print(self.cnt, '권 (1)')

    @classmethod
    def output2(cls): #class는 인자를 self로 안받고  cls로 받음
        cls.cnt += 1
        print('(2) 총', cls.cnt , '권')



b1 = Book('행복이란')
b2 = Book('먹고살자')

b1.output()
b2.output()

b1.output2()
b2.output2()
#Book.output() #output 함수에는 @classmethod를 붙이지 않았기 때문에 인스턴스 함수라 이렇게 부를 수 없음
Book.output2()


'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
            -오버로딩(Overloading) : 같은 이름의 메서드 여러개를 가지면서 매개변수의 유형과 개수가 다르도록 하는 기술
            -오버라이딩(Overriding) : 상위 클래스가 가지고 있는 메서드를 하위 클래스가 재정의해서 사용
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''

class Animal:
    def move(self):
        print('동물은 움직인다')

class Wolf(Animal): #상속 Animal클래스가 부모클래스가 됨
    def move(self):
        print('늑대는 4발로 달린다')

w = Wolf()
w.move()

class Human(Animal):
    def move(self):
        print('인간은 2발로 달린다')

class WolfHuman(Human,Wolf):
    pass #비어있는 클래스 만드려면 그냥 pass만 적어두면 됨

wh = WolfHuman()
wh.move() #WolfHuman()은 Animal과 Human을 상속받음 WolfHuman클래스의 ()안에 들어있는 순서에 따라 제일 처음있는것을 가져옴

#+++++++++++++++(1)
class Person:
    def greeting(self):
        print('안녕하세요.')


class University:
    def manage_credit(self):
        print('학점 관리')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james = Undergraduate()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()  # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드

#+++++++++++++++(2)
#다이아몬드 상속
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')


class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')


class D(B, C):
    pass


x = D()
x.greeting()  # 안녕하세요. B입니다.

