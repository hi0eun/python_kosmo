"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url) #parse란 뭔가를 쪼개는 것
    print('1-', p)
    #1- ParseResult(scheme='https', netloc='docs.python.org', path='/3.6/library/', params='', query='', fragment='')
    savepath = './' + p.netloc + p.path
    print('2-', savepath)

    if re.search('/$',savepath): #$가 끝나는것을 의미함 /$=> /로 끝나면 index.html이 빠진것
        savepath += 'index.html'
        print('3-',savepath)

    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    if os.path.exists(savepath): return savepath

    try:
        request.urlretrieve(url,savepath)
        time.sleep(2)
        return savepath
    except:
        print('failed download..', url)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



