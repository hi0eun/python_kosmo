import  cx_Oracle as oci

#[DB 연동 절차]
# 1. Connection 얻어오기
conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
#('계정명/비밀번호@포트번호/오라클명') 오라클의 포트번호 : 1521
print(conn.version)
#오라클이 제대로 연결되었는지 확인하는 법 제대로연결 시 오라클 버전 출력함

# 2. sql 문장 만들기 (대소문자 안가림)
sql = 'SELECT * FROM EMP'

# 3. cursor 얻어오기 -> 자바에서의 전송객체 얻어오기 대신일 수도
cursor = conn.cursor()

# 4. sql 실행(전송)
'''
cursor.execute(sql)
for row in cursor:
    print('사번:',row[0],'사원명:',row[1])
'''
cursor.execute(sql)
datas = cursor.fetchall()
for row in datas:
    print('사번:',row[0],'사원명:',row[1])

# 5. cursor닫기
cursor.close()
# 6. 연결 닫기
conn.close()
