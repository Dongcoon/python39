# 2차원 배열과 dict을 사용한 성적 처리
sjs = []
sel = 0
while True:
    sel = int(input('메뉴선택 > '))
    if sel == 1:
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
        if avg >= 90: grd = '수'
        elif avg >= 80: grd = '우'
        elif avg >= 70: grd = '미'
        elif avg >= 60: grd = '양'

        # 데이터 저장
        sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat,
              'tot': tot, 'avg': avg, 'grd': grd}

        sjs.append(sj)

        # 결과 출력
    elif sel == 2:
        for sj in sjs:
            print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}')
    elif sel == 3:
        name = input('조회할 학생의 이름은?')

        sj = None
        for item in sjs:
            if item['name'] == name: sj = item
        hdr = '이름   국어  영어  수학  총점  평균  학점\n'
        hdr += '----------------------------\n'
        print(hdr,end='')
        for k in sj.keys():
            print(sj.get(k), end='  ')

        input('\n 상세 조회 완료!!')
    elif sel == 4:
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
    elif sel == 5:
        name = input('삭제할 데이터의 학생이름은?')

        idx = None
        for i in range(len(sjs)):
            item = sjs[i]
            if item['name'] == name:
                idx = i

        sjs.pop(idx)

        input('성적 데이터 삭제 완료!!')
