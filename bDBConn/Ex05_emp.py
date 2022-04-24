import pymysql

config = {
     'host' : '127.0.0.1',
     'user' : 'scott',
     'password' : 'tiger',
     'database' : 'scott',
     'port' : 3306,
     'charset':'utf8',
     'use_unicode' : True}


def set_contact():
    # 여기에 코드 작성
    empno = input("사번 입력 ->")
    ename = input("사원 이름 ->")
    job = input("사원 업무 ->")
    deptno = input("부서 번호 ->")
    # contact = empno, ename, job, deptno  # 입력한 정보가 클래스 인스턴스로 생성
    # return contact
    # 1. Connection 얻어오기
    conn = pymysql.connect(**config)
    #다른방법
    #conn = pymysql.connect(host='127.0.0.1', user='root',password='admin1234',db='scott',charset='utf8')

    # 2. sql 문장 만들기
    sql ='''
    INSERT INTO emp (empno,ename,job,deptno)
    VALUES( "{}", "{}", "{}", "{}" )
    '''.format(empno,ename,job,deptno)

    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.commit()
    conn.close()


def print_contact():
    # 여기에 코드 작성
    # 1. Connection 얻어오기
    conn = pymysql.connect(**config)
    # 2. sql 문장 만들기
    sql = 'SELECT * FROM EMP'

    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    print('-' * 50)
    print('사번', '이름', '업무', '부서번호')
    print('-' * 50)
    for row in cursor:
        print(row[0],row[1],row[2],row[7])
    print('-' * 50)
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.close()


def delete_contact():
    # 여기에 코드 작성
    empno=input('삭제할 사원의 사번을 입력하세요 ->')

    # 1. Connection 얻어오기
    conn = pymysql.connect(**config)
    # 2. sql 문장 만들기
    sql = '''
        delete
        from emp
        where empno = {}
        '''.format(empno)

    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.commit()
    conn.close()

def print_menu():
    print('1. 사원정보 입력')
    print('2. 사원정보 출력')
    print('3. 사원정보 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)


def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            delete_contact()


if __name__ == "__main__":
    run()
