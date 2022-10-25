from SungJukVO import SungJukVO
from SungJukV8DAO import SungJukV8DAO as sjdao

class SungJukV8Lib:
    @staticmethod
    def display_menu():
        main_menu = f'''성적 처리 프로그램 v8
    ------------------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    ------------------------'''
        print(main_menu)

        return input('=> 메뉴를 선택해주세요: ')

    # private function 으로 선언
    @staticmethod
    def __input_sungjuk():
        name = input('이름: ')
        kor = int(input('국어 성적: '))
        eng = int(input('영어 성적: '))
        mat = int(input('수학 성적: '))

        return SungJukVO(name, kor, eng, mat)

    @staticmethod
    def add_sungjuk():
        print(' == 학생 및 성적 정보 입력 == ')
        # 성적 데이터 입력 받기
        sj = SungJukV8Lib.__input_sungjuk()

        # 입력받은 성적데이터 초기화
        SungJukV8Lib.__complute_sungjuk(sj)

        # 성적 데이터 테이블에 저장
        if sjdao.insert_sungjuk(sj) > 0:
            print('성적데이터 추가 완료')

    @staticmethod
    def read_sungjuk():
        hdr = '이름\t\t총점\t\t등급\n'
        hdr += '----------------------'
        print(hdr)

        rows = sjdao.select_sungjuk()

        result = ''
        for row in rows:
            result += f'{row[0]}    {row[1]}    {row[2]}\n'

        print(result)


    def __complute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        grd = '가'
        if sj.avg >= 90:
            sj.grd = '수'

        elif sj.avg >= 80:
            sj.grd = '우'

        elif sj.avg >= 70:
            sj.grd = '미'

        elif sj.avg >= 60:
            sj.grd = '양'

        return sj.tot, sj.avg, sj.grd


    @staticmethod
    def read_one_sungjuk():
        name = input('조회할 학생의 이름은?')


        hdr = '번호\t이름\t국어\t영어\t수학\t총점\t평균\t등급\n'
        hdr += '------------------------------------------------------'
        print(hdr)

        row = sjdao.select_one_sungjuk(name)

        result = f'{row[0]}    {row[1]}    {row[2]}    {row[3]}    {row[4]}    {row[5]}    {row[6]:.1f}    {row[7]} '

        print(result)

    @staticmethod
    def modify_sungjuk():
        name = input('수정할 학생 이름: ')

        # 수정할 학생 이름으로 기존데이터 조회
        sj = sjdao.select_one_sungjuk(name)
        # 새로운(기존) 값을 입력받음
        kor = int(input(f'새로운 국어는? ({sj[2]})'))
        eng = int(input(f'새로운 영어는? ({sj[3]})'))
        mat = int(input(f'새로운 수학는? ({sj[4]})'))

        # 다시 성적 처리
        sj = SungJukVO(name, kor, eng, mat)
        SungJukV8Lib.__complute_sungjuk(sj)

        cnt = sjdao.update_sungjuk(sj)



        if cnt > 0: print('성공적으로 수정 했따')

    @staticmethod
    def remove_sungjuk():
        name = input('삭제할 데이터의 학생 이름을 입력하세요: ')

        # 삭제할 학생이름을 입력받아 성적테이블에서 해당 학생 데이터 삭제
        cnt = sjdao.delete_sungjuk(name)

        if cnt > 0:
            print('성공적으로 삭제되었습니다.')