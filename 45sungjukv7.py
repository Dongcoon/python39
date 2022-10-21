# csv 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv7lib.py에 작성하고
# 모듈명은 sjv7로 줄여서 사용함

import sungjukv7lib as sjv7

# 프로그램 주 실행부
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv7.displayMenu()

    if menu == '1': sjv7.addSungJuk()
    elif menu == '2': sjv7.readSungJuk()
    elif menu == '3': sjv7.readOneSungJuk()
    elif menu == '4': sjv7.modifySungJuk()
    elif menu == '5': sjv7.removeSungJuk()
    elif menu == '6': break