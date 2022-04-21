with open('dream.txt', 'rt', encoding='utf-8') as f:
    lines = f.readlines()
    for i , contact in enumerate(lines):
        print("{}--{}".format(i,contact))



    try:
        with open('dream.txt', 'rt', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print('해당파일이 존재하지 않습니다')
    else:
        wcnt = len(content.split())
        print("총 단어 수 :",wcnt)
        print("총 줄 수 :",contact.count("\n")+1)