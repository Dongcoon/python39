# 파이썬으로 데이터 다루기 2 - insert
# 입력한 회원정보를 member 테이블에 저장
import sqlite3

# 회원정보 입력받기
userid = input('아이디는 > ')
passwd = input('패스워드는 >')
name = input('이름은 >')
email = input('이메일은 >')

conn = sqlite3.connect('C:/Java/bigdata.db')
cur = conn.cursor()
# 매개변수 placeholder(?)를 이용해서 실제 값 지정
sql = f'insert into member values (?,?,?,?)'
params = (userid, passwd,name,email)

# sql injection 공격의 위험 존재!
# sql = f'insert into member values ({userid},{passwd},{name},{email}) ; '

cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출
print(cur.rowcount,'행이 추가됨')

cur.close()
conn.close()


# 파이썬으로 데이터 다루기 3 - update
# 수정할 회원의 아이디를 입력받아 회원정보 수정
import sqlite3

# 수정할 회원아이디
userid = input('수정할 아이디는?')

# 회원정보 입력받기
passwd = input('패스워드는 >')
name = input('이름은 >')
email = input('이메일은 >')

conn = sqlite3.connect('C:/Java/bigdata.db')
cur = conn.cursor()
# named parameter placeholder(?)를 이용해서 실제 값 지정
sql = f'update member set passwd = :pwd, name = :name, email = :eml where userid = :uid'
params = {'pwd':passwd, 'name':name, 'eml':email, 'uid':userid}

cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출

cur.close()
conn.close()

# 파이썬으로 데이터 다루기 4 - delete
# 삭제할 회원의 아이디를 입력받아 회원정보 삭제
import sqlite3

# 삭제할 회원아이디
userid = input('삭제할 아이디는?')

conn = sqlite3.connect('C:/Java/bigdata.db')
cur = conn.cursor()
# named parameter placeholder(?)를 이용해서 실제 값 지정
sql = f'delete from member where userid = :uid '
params = {'uid':userid}

cur.execute(sql, params)
conn.commit()    # 테이블에 값 저장하기 위해 commit 호출

cur.close()
conn.close()