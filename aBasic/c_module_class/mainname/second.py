import first  # first 모듈을 가져옴

print('second.py __name__:', __name__)  # __name__ 변수 출력
#자기 파일에서 __name__ 출력하면 __main__이 출력되고 다른 파일에서 출력되면 자기 파일의 이름이 출력됨
#import 한 first 파일 내용
'''print('first 모듈 시작')
print('first.py __name__:', __name__)    # __name__ 변수 출력
print('first 모듈 끝')'''
#위의 first의 실행문들이 second에서 실행될 때는
# first파일의 print('first.py __name__:', __name__)의 __name__은 first파일의 이름인 first가 되고
#second파일의 print('second.py __name__:', __name__)의 __name__은 자기 자신 파일의 실행문이기 때문에 __main__이 되는것임