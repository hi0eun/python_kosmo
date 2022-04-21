"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""

#년 월 일
from datetime import  date
today = date.today()
print('today is ', today)
print('today is ', today.year)
print('today is ', today.month)
print('today is ', today.day)

#시 분 초
from datetime import datetime,timedelta
today = datetime.today()
print('today is ', today.hour)
print('today is ', today.minute)
print('today is ', today.second)

#오늘 날짜부터 10일 후
print('today + 10d is ',today + timedelta(days=10))
print('today - 10d is ',today + timedelta(days=-10))

#오늘 날짜부터 3개월 후
# print('today + 3m is ',today + timedelta(months=3)) => 에러발생
# python-dateutil 패키지를 추가 설치 필요
#->File | Settings | Project: aBasic | Python Interpreter -> + -> dateutil검색 -> python-dateutil선택 후 install package
from dateutil.relativedelta import relativedelta
print(today + relativedelta(months=3))

