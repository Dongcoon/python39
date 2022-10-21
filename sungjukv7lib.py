import pymysql

def displayMenu():
    main_menu = f'''
    성적 처리 프로그램 v6
    ----------------
    1. 성적 데이터 등록
    2. 성적 데이터 조회
    3. 성적 데이터 검색
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    6. 종료
    '''
    print(main_menu)
    menu = input('입력 >')
    return menu


def inputSungJuk():
    # 데이터 입력
    name = input('이름: ')
    kor = int(input('국어: '))
    eng = int(input('영어: '))
    mat = int(input('수학: '))
    # sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    sj = [name, kor, eng, mat]
    return sj

def addSungJuk():
    print('성적 등록')

    sj = inputSungJuk()

    url = 'bigdata.ccdt7ih2qkyl.ap-northeast-2.rds.amazonaws.com'
    userid = 'admin'
    passwd = 'Bigdata_2022'
    dbname = 'bigdata'

    conn = pymysql.connect(host=url, user=userid, password=passwd,
                           database=dbname, charset='utf8')

    cur = conn.cursor()
    sql = 'insert into sungjuk(name,kor,eng,mat,' \
          's_tot,s_avg,s_grd) values()'
    cur.execute(sql)

    # 성적 처리
    tot,avg,grd = computeSungJuk(sj)

    # sj['tot'], sj['avg'], sj['grd'] = result[0], result[1], result[2]
    # + : 2개의 리스트를 하나로 합쳐 하나의 리스트로 만듦
    sj = sj + [tot,avg,grd]

    # 처리된 입력한 성적데이터를 sungjuk 테이블에 저장
    # pass

def readSungJuk():
    hdr = '이름 국어 영어 수학 \n'
    hdr += '----------------------\n'
    print(hdr, end='')
    # 성적테이블에서 이름/국어/영어/수학 만 select해서 출력
    input('성적데이터 조회완료')


def readOneSungJuk():
    name = input('조회할 학생의 이름은?')


    hdr = '이름   국어  영어  수학  총점  평균  학점\n'
    hdr += '----------------------------\n'
    print(hdr, end='')
    # 입력한 학생이름으로 성적테이블을 조회해서
    # 조회된 결과를 출력

    input('\n 상세 조회 완료!!')


def modifySungJuk():

    name = input('수정할 학생의 이름은?')

    # 수정할 학생이름으로 기존데이터 조회

    # 새로운(기존) 값을 입력받음
    kor = int(input(f'새로운 국어는?() '))
    eng = int(input(f'새로운 영어는?() '))
    mat = int(input(f'새로운 수학은?() '))

    # 다시 성적 처리
    sj = [name, kor, eng, mat]
    tot,avg,grd = computeSungJuk(sj)
    sj = sj + [tot, avg, grd]

    # 새롭게 입력된 성적데이터를
    # 기존 성적데이터에 반영함


def removeSungJuk():
    name = input('삭제할 데이터의 학생이름은?')

    # 삭제할 학생이름 입력받아서
    # 성적테이블에서 해당 데이터 삭제

    input('성적 데이터 삭제 완료!!')

# 세부 기능
def computeSungJuk(sj):
    tot = sj[1] + sj[2] + sj[3]
    avg = tot / 3
    grd = '가'
    if avg >= 90: grd = '수'
    elif avg >= 80: grd = '우'
    elif avg >= 70: grd = '미'
    elif avg >= 60: grd = '양'
    return tot,avg,grd