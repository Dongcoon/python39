# 파이썬 데이터베이스 프로그래밍
# 데이터의 영속성을 부여하는 방법 중 하나
# 작은 양의 데이터는 파일입출력을 통해 처리 가능
# 대량의 데이터를 체계적으로 저장해서 원하는 목적에 따라
# 데이터를 처리(검색,수정,삭제)할 수 있도록 해 줌

# 파이썬에서는 일반적인 관계형 데이터베이스를 이용해서
# 데이터를 저장,검색,수정,삭제할 수 있음
# 또한, 독립적인 데이터베이스 서버없이 파일기반
# 데이터베이스를 이용해서 간편하게 데이터를 조작할 수도 있음
# 내장형 파일기반 데이터베이스 : sqlite

# sqlite
# 내장형 파일기반 데이터베이스
# 서버가 필요없고 복잡한 설정도 필요없으면서
# 트랜잭션이 지원되는 데이터베이스
# 하나의 파일에 테이블,뷰,색인,트리거등이 저장
# 용량이 작아 메모리에 올리기도 쉽고 속도도 빠른편
# 안드로이드, ios에는 기본적으로 포함되어 있음
# 단, 복잡하고 용량이 큰 데이터를 저장하기에는 다소 적절치 않음
# sqlite.org

# sqlite 설치법
# sqlite-tools-win32-x86-3370200.zip  (2022.2.14기준)
# 압축해제 후 sqlit3.exe를 c:/Java 에 저장
# 명령프롬프트에서 sqlite3.exe를 실행 함
# => cd \Java

# 데이터베이스 생성: .open 디비명.db
# .open bigdata.db

# 테이블 생성 : create table
#create table member (
#    userid varchar(18) primary key,
#    passwd varchar(18) not null,
#    name varchar(18) not null,
#   email varchar(18) not null
# );

# 테이블 목록 확인 : .table

# 테이블 구조 확인 : pragma table_info('테이블명');
# pragma table_info('member');

# 조회시 컬럼헤더 설정
# .header on
# .mode column

# 데이터 삽입
# insert into member values (
# 'abc123', '987xyz', 'abc123', 'abc@xyz.com');

# 데이터 조회
# select * from memver;

# csv 파일 가져오기
# .mode csv
# .import csv파일명 테이블명
# employees.csv, summermedals.csv smd
# .import c:/Java/EMPLOYEES.csv emp

# tsv 파일 가져오기 - 탭으로 구분된 파일
# .mode tabs
# .import tsv파일명 테이블명

# 데이터베이스 종료 : .quit

# 파이썬으로 데이터 다루기 1 - select
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('C:/Java/bigdata.db')

# SQL 실행을 위해 커서 생성
cur = conn.cursor()

# 실행할 SQL문을 작성하고
# 실행후 결과를 커서에 저장
sql = 'select * from member'
cur.execute(sql)

# 반복문 이용해서 커서에 저장된
# 결과집합으로 부터 한행씩 읽어와서 처리
while True:
    row = cur.fetchone()    # 커서에서 한 건 읽어온 후
    if not row : break      # 내용이 없으면 반복 중단
    # 읽어온 결과에서 각 컬럼값을 변수에 저장하고 출력
    result = f'{row[0]} {row[1]} {row[2]} {row[3]}'
    print(result)

# 반복실행 종료시 커서 사용종료
cur.close()

# 데이터베이스 사용종료
conn.close()

# ex) 직책별 사원수 조회 : emp
import sqlite3
conn = sqlite3.connect('C:/Java/bigdata.db')
cur = conn.cursor()
sql = 'select count(EMPLOYEE_ID) as cnt , JOB_ID from emp group by job_id order by cnt desc'
cur.execute(sql)
print('사원수 직책 ')
while True:
    row = cur.fetchone()    # 커서에서 한 건 읽어온 후
    if not row : break      # 내용이 없으면 반복 중단
    # 읽어온 결과에서 각 컬럼값을 변수에 저장하고 출력
    result = f'{row[0]}      {row[1]}'
    print(result)
cur.close()
conn.close()

# ex) 국가별 금메달 수상수 조회(상위 10개국만) 1 : fetchone
import sqlite3
conn = sqlite3.connect('C:/Java/bigdata.db')
cur = conn.cursor()
medal = 'Gold'
result = ''
sql = f'select Country, count(*) as cnt from smd where Medal = "{medal}" GROUP BY Country order by cnt desc limit 10 ; '
cur.execute(sql)
print('나라 금메달(수) ')
while True:
    row = cur.fetchone()    # 커서에서 한 건 읽어온 후
    if not row : break      # 내용이 없으면 반복 중단
    # 읽어온 결과에서 각 컬럼값을 변수에 저장하고 출력
    result += f'{row[0]}  {row[1]}\n'

cur.close()
conn.close()
print(result)

# ex) 국가별 금메달 수상수 조회(상위 10개국만) 2 : fetchall
import sqlite3

conn = sqlite3.connect('C:/Java/bigdata.db')
cur = conn.cursor()
medal = 'Gold'
result = ''
sql = f'select Country, count(*) as cnt from smd where Medal = "{medal}" GROUP BY Country order by cnt desc limit 10 ; '
cur.execute(sql)
print('나라 금메달(수) ')
rows = cur.fetchall()  # 커서에서 한 건 읽어온 후
for row in rows:
    result += f'{row[0]}  {row[1]}\n'

cur.close()
conn.close()
print(result)

