pin = '880122-1234567'

birthday = "홍길동님 생년월일: {}".format(pin[:6])
if pin[-7] == "1" or pin[-7] == "3":
    gender = "성별 : 남자"
else:
    gender = "성별 : 여자"

print(birthday)
print(gender)

'''[출력결과]
홍길동님
생년월일: 880122
성별: 남자'''

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

a = ['독도는','대한민국의','아름다운','섬입니다']
result = " ".join(a)
print( result )

a = (1, 2, 3)
a = a + (4,)
print(a)

a = b = [1, 2, 3]
a[1] = 4
print(b)


life = {
    'animals': {
        'cats': [
            'Kim','Lee','Choi'
                ],
        'octopi': {},
        'emus': {}
        },
    'plants': {},
    'other': {}
}

print(life)

kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]
midterm_score = [kor_score, math_score, eng_score]

print(midterm_score)

sjname = ["kor_score", "math_score", "eng_score"]
#과목별 총합과 평균
for i in range(len(midterm_score)):
    sjsum=sum(midterm_score[i])
    print("{sjname}의 총합은 {sjsum}\n"
          "{sjname}의 평균은 {sjavg}".format(sjname=sjname[i],sjsum=sjsum,sjavg=sjsum/len(midterm_score[i])))

#학생별 총합과 평균
for i in range(len(kor_score)):
    stsum=[]
    for j in range(len(midterm_score)):
       stsum.append(midterm_score[j][i])
    print("{idx}번째 학생의 점수총합은:{sum}\n{idx}번째 학생의 점수평균은:{avg}".format(idx=i+1,sum=sum(stsum),avg=sum(stsum)/len(midterm_score)))



for i in range(3):

    try:

        print(i, 3// i)

    except ZeroDivisionError:

        print("Not divided by 0")