# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }

s = set()               # 빈 집합을 생성
#s = {}                  # ????????????? set인지 dictionary인지
#print(type(s))         # dictionary임
# set인지 dirctionary인지 상관없긴 함  왜? 파이썬과 자바스크립트는 자료형 변경이 가능하기 때문 => a= 1 하고 a = "일" 이렇게하면 그대로 값이 들어감


s = set([1,2,3,1,1])
print(s) #{1,2,3}
# print(s[0]) #오류남 왜? set은 인덱스가 없음

#     -리스트는 중복이 가능 set은 중복 불가능
#     -리스트는 대괄호 set은 중괄호
#     -리스트는 인덱스가 있지만 set은 인덱스가 없음

b = { 3,4,5,6 }

print(s.intersection(b)) #교집합
print(s.union(b)) #합집합

print( s | b )  #합집합 or
print( s & b )  #교집합 and

print( s - b ) #차집합
print( b - s ) #차집합