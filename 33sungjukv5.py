# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv5lib.py에 작성하고
# 모듈명은 sjv5로 줄여서 사용함

# 프로그램 주 실행부
import sungjukv5 as sjv5

sjs = []
while True:
    # 메뉴 표시 및 값 입력
    # 메뉴 입력받음
    menu = sjv5.displayMenu()

    if menu == '1': sjv5.addSungJuk(sjs)
    elif menu == '2': sjv5.readSungJuk(sjs)
    elif menu == '3': sjv5.readOneSungJuk(sjs)
    elif menu == '4': sjv5.modifySungJuk(sjs)
    elif menu == '5': sjv5.removeSungJuk(sjs)
    elif menu == '0': break