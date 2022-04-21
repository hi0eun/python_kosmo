#Ex03_sample.py
import cx_Oracle as oci
import csv

def createTable():
    # 1. Connection 얻어오기
    conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장 만들기
    sql = """
        create table supply
        (
            id      integer     primary key,
            supplier_name   varchar(30),
            invoice_number  varchar(20),
            part_number     varchar(30),
            cost    integer,
            purchase_date   date
        )
    """
    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    #---------------------------------
    #시퀀스 생성
    sql2='CREATE SEQUENCE SEQ_SUPPLY_ID'
    cursor.execute(sql2)
    #---------------------------------
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.close()

def saveTable(data):
    # 1. Connection 얻어오기
    conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장 만들기
    sql = '''
    INSERT INTO supply (id,supplier_name,invoice_number,part_number,cost,purchase_date)
    VALUES( SEQ_SUPPLY_ID.nextval, :0, :1, :2, :3, :4 ) 
    '''
    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql, data)
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.commit() #커밋
    conn.close()

def viewTable(tname):
    # 1. Connection 얻어오기
    conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장 만들기
    sql = 'SELECT * FROM {}'.format(tname)
    # 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    #sql문장만들기에서 :0 :1~~ 쓰려면 cursor.execute(sql, 튜플이어야함)
    #cursor.execute(sql) 이렇게 쓰려면 sql문장 만들때 .format(tname)쓰기 
    for row in cursor:
        print(row)
    # 5. cursor닫기
    cursor.close()
    # 6. 연결 닫기
    conn.close()

if __name__ == '__main__': #JAVA의 메인함수와 유사
    #createTable()
    #imsi = ['kosmo','9999','8888',1000,'2022-04-20']
    #saveTable(imsi)
    viewTable('supply')

   # file = open('./files/supply.csv','r')
   #  datas = csv.reader(file,delimiter=',')
   #  #csv파일의 데이터를 구분문자(delimiter) ','를 기준으로 읽겠다.
   #  header = next(datas, None)
   #  # csv파일 첫 줄 가져오기 None = 아무일도 안함
   #  # =>첫줄을 가져와서 아무일도 안하게하겠다 => 첫줄을 빼겠다
   #  # 만약에 그 제목이 필요하면 변수 지정 필요없으면 지정안해도됨
   #  print('제목',header)
   #  #지금 당장 제목 필요없지만 한 번 해본 것
   #
   #  for row in datas:
   #      saveTable(row)
   #  #csv파일에서 ','를 기준으로 가져온 데이터들을 하나하나 입력하겠다



