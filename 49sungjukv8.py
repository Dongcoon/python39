# 마리아디비를 이용한 성적처리 프로그램
# 성적 처리 프로그램의 함수들은 sungjukv7lib.py에 작성함
# 모듈명은 sjv7로 줄여서 사용함

# 성적데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부

# 파일에 저장된 성적데이터 불러오기
# 프로그램 시작전 데이터 초기화
from SungJukV8Lib import SungJukV8Lib as sjv8

# 파일에 저장된 성적데이터 불러오기
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv8.display_menu()

    if menu == '1':
        sjv8.add_sungjuk()
    elif menu == '2':
        sjv8.read_sungjuk()
    elif menu == '3':
        sjv8.read_one_sungjuk()
    elif menu == '4':
        sjv8.modify_sungjuk()
    elif menu == '5':
        sjv8.remove_sungjuk()
    elif menu == '0':
        break
    else:
        print('잘못된 입력입니다.')