# mariaDB로 데이터 다루기 1 - select
# pymysql 모듈을 먼저설치: pip install pymysql
import pymysql

url = 'bigdata.ccdt7ih2qkyl.ap-northeast-2.rds.amazonaws.com'
userid = 'admin'
passwd = 'Bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url,user=userid,password=passwd,
                       database=dbname,charset='utf8')

cur = conn.cursor()
sql = 'select userid, passwd, name, email from member'
cur.execute(sql)

result = ''
rows = cur.fetchall()  # 커서에서 한 건 읽어온 후
for row in rows:
    result += f'{row[0]}  {row[1]}  {row[2]}    {row[3]}\n'

cur.close()
conn.close()

print(result)

# mariaDB로 데이터 다루기 2 - insert
import pymysql


url = 'bigdata.ccdt7ih2qkyl.ap-northeast-2.rds.amazonaws.com'
userid = 'admin'
passwd = 'Bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url,user=userid,password=passwd,
                       database=dbname,charset='utf8')
# 회원정보 입력받기
uid = input('아이디는 > ')
pwd = input('패스워드는 >')
name = input('이름은 >')
email = input('이메일은 >')

cur = conn.cursor()
# 매개변수 placeholder(%)를 이용해서 실제 값 지정
sql = f'insert into member(userid, passwd,name,email)' \
      f' values (%s, %s, %s, %s)'
params = (uid, pwd,name,email)

cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출
print(cur.rowcount,'행이 추가됨')

cur.close()
conn.close()

# mariaDB로 데이터 다루기 3 - update
import pymysql


url = 'bigdata.ccdt7ih2qkyl.ap-northeast-2.rds.amazonaws.com'
userid = 'admin'
passwd = 'Bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url,user=userid,password=passwd,
                       database=dbname,charset='utf8')
# 수정 아이디 입력
uid = input('수정할 아이디 >  ')

# 수정정보 입력받기
pwd = input('패스워드는 >')
name = input('이름은 >')
email = input('이메일은 >')

cur = conn.cursor()
# 매개변수 placeholder(%)를 이용해서 실제 값 지정
sql = f'insert into member(userid, passwd,name,email)' \
      f' values (%s, %s, %s, %s)'
params = (uid, pwd,name,email)

cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출
print(cur.rowcount,'행이 추가됨')

cur.close()
conn.close()

