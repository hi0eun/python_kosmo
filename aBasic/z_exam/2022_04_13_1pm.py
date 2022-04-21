# 1. 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.
# 또 숫자중에서 평균을 출력하여 보자.

a = 0
for i in range (1,6):
    i = int(input('정수를 입력하세요: '))
    a = a + i
print(a/5)
print()

#2. 사용자에게서 받은 문자들을 역순으로 출력한다.
f = input('문자를 입력하시오')

print(f[::-1])

#이 아래부턴 인터넷에서 가져옴
#3. 사용자에게서 받은 정수들의 평균과 표준편차를 계산하여 출력한다.
#평균과 표준편차를 프로그램을 작성하세요
arr = input('정수리스트 입력 : ').split()
a = int(arr[0])
b = a + int(arr[1])
c = b + int(arr[2])
d = c + int(arr[3])
e = d + int(arr[4])
avg = e / 5
print('평균 : ', avg)
bunsan = ( (a-avg)**2 + (b-avg)**2 + (c-avg)**2 + (d-avg)**2 + (e-avg)**2 )/5
print(bunsan)
pyuncha = bunsan ** (1/2)
print('표준편차 : ', pyuncha)

#4전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.
phone = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
string = input('문자열을입력하시오: ')
result = ''
for char in string:
    for i in range(len(phone)):
        if char.upper() in phone[i]:
            result += str(i + 1)
print(result)