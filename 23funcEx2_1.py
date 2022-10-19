# 함수 정의부
def displayMenu():
    main_menu = f'''
    성적 처리 프로그램 v4
    ----------------
    1. 성적 데이터 등록
    2. 성적 데이터 조회
    3. 성적 데이터 검색
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    '''
    print(main_menu)


def addSungJuk():
    print('성적 등록')

    # 데이터 입력
    name = input('이름: ')
    kor = int(input('국어: '))
    eng = int(input('영어: '))
    mat = int(input('수학: '))

    # 성적 처리
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    # 데이터 저장
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat,
          'tot': tot, 'avg': avg, 'grd': grd}

    sjs.append(sj)


def readSungJuk():
    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}')


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
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    # 값 다시 저장
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat,
          'tot': tot, 'avg': avg, 'grd': grd}

    # 기존에 저장되어있던 위치에 다시 저장

    sjs[idx] = sj


def removeSungJuk():
    name = input('삭제할 데이터의 학생이름은?')

    idx = None
    for i in range(len(sjs)):
        item = sjs[i]
        if item['name'] == name:
            idx = i

    sjs.pop(idx)

    input('성적 데이터 삭제 완료!!')


# 프로그램 주 실행부
sjs = []
while True:
    # 메뉴 표시 및 값 입력
    # 메뉴 입력받음
    displayMenu()
    menu = input('=> 메뉴를 선택하세요 : ')

    if menu == '1': addSungJuk()
    elif menu == '2': readSungJuk()
    elif menu == '3': readOneSungJuk()
    elif menu == '4': modifySungJuk()
    elif menu == '5': removeSungJuk()
    elif menu == '0': break