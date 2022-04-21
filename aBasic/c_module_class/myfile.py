#myfile.py

'''import mymodule

print('오늘의 날씨는',mymodule.get_weather())
print('오늘의 요일은',mymodule.get_date())'''

#mymodule의 print가 있으면 그것도 포함해서 결과가 나오고
#이 파일에서 print 안했을 경우 mymodule의 print가 결과로 나옴

'''from mymodule import get_weather , get_date

print('오늘의 날씨는',get_weather())
print('오늘의 요일은',get_date()) '''

#from import를 쓸경우 딱 그 import한 것만 가능함으로 get_date() 불가능 가능하게하려면 import get_weather에 ,찍고 get_date해줘함

#별칭 주기
'''from mymodule import mymodule as mm #mypackage

print('오늘의 날씨는',mm.get_weather())
print('오늘의 요일은',mm.get_date())'''
#별칭 줄 경우 원래 이름 안먹히고 별칭만 먹힘


#------------c_modul_class에 있는 mymodule파일을 c_module_class의 파이썬 패키지 mypackage에 옮겼을 때
'''
#방법1
#from c_module_class.mypackage import mymodule #되지만
from mypackage import mymodule #myfile과 mypacakge는 형제관계이기 때문에 이렇게 써도 가능 
print('오늘의 날씨는',mymodule.get_weather())
print('오늘의 요일은',mymodule.get_date())'''

#방법2
'''import mypackage.mymodule 
print('오늘의 날씨는',mypackage.mymodule.get_weather())
print('오늘의 요일은',mypackage.mymodule.get_date())'''

#방법1과 같음
from mypackage import mymodule

print('오늘의 날씨는',mymodule.get_weather())
print('오늘의 요일은',mymodule.get_date())