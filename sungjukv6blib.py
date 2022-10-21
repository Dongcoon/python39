import json
# 성적 데이터 저장할 변수 선언
sjs = []

# sungjuk.dat 파일을 읽어서 sjs변수에 초기화
def loadSungJuk():
    global sjs

    # 파일에 저장된 성적데이터들을 모두 읽어 리스트에 저장
    try :
        with open('data/sungjukv6b.dat', encoding='UTF=8') as f:
            data = f.read()
            sjs = json.load( data )
    except:
        pass

# 성적데이터들을 sungjukv6b.dat 파일에 저장
# [{'name': name, 'kor': kor, 'eng': eng, 'mat': mat},
# {'name': name, 'kor': kor, 'eng': eng, 'mat': mat},
# {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}]
def saveSungJuk(sjs):
    with open('data/sungjuk.datv6b', 'w', encoding='UTF-8') as f:
        # 방금 입력한 성적데이터와
        # 기존에 입력한 모든 성적데이터를 파일에 함께 저장
        f.write( json.dumps(sjs, ensure_ascii = False))

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
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    return sj

def addSungJuk():
    print('성적 등록')

    sj = inputSungJuk()

# 성적 처리
    result = computeSungJuk(sj)
    sj['tot'], sj['avg'], sj['grd'] = result[0], result[1], result[2]

    sjs.append(sj)

    # sjs에 저장된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

def readSungJuk():
    hdr = '이름   국어  영어  수학 \n'
    hdr += '----------------------\n'
    print(hdr, end='')
    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]} {sj["tot"]} {sj["avg"]} {sj["grd"]}')
    input('성적데이터 조회완료')


def readOneSungJuk():
    name = input('조회할 학생의 이름은?')
    sj = None
    for item in sjs:
        if item['name'] == name: sj = item
    hdr = '이름   국어  영어  수학  총점  평균  학점\n'
    hdr += '----------------------------\n'
    print(hdr, end='')
    for k in sj.keys():
        print(sj.get(k), end='  ')

    input('\n 상세 조회 완료!!')


def modifySungJuk():

    name = input('수정할 학생의 이름은?')

    sj = None

    idx = None
    for i in range(len(sjs)):
        if sjs[i]['name'] == name:
            idx = i
            break

    # 새로운(기존) 값을 입력받음
    kor = int(input(f'새로운 국어는?({sjs[idx]["kor"]}) '))
    eng = int(input(f'새로운 영어는?({sjs[idx]["eng"]}) '))
    mat = int(input(f'새로운 수학은?({sjs[idx]["mat"]}) '))

    # 다시 성적 처리
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    result = computeSungJuk(sj)
    sj['tot'],sj['avg'],sj['grd'] = result[0],result[1],result[2]

    # 기존에 저장되어있던 위치에 다시 저장
    sjs[idx] = sj

    # 수정된 성적데이터를 파일에 저장
    saveSungJuk(sjs)


def removeSungJuk():
    name = input('삭제할 데이터의 학생이름은?')

    idx = None
    for i in range(len(sjs)):
        item = sjs[i]
        if item['name'] == name:
            idx = i

    sjs.pop(idx)

    # 삭제된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

    input('성적 데이터 삭제 완료!!')

# 세부 기능
def computeSungJuk(sj):
    tot = sj['kor'] + sj['eng'] + sj['mat']
    avg = round(tot // 3)
    grd = '가'
    if avg >= 90: grd = '수'
    elif avg >= 80: grd = '우'
    elif avg >= 70: grd = '미'
    elif avg >= 60: grd = '양'
    return tot,avg,grd