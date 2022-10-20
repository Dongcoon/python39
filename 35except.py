# 예외처리
# 프로그램을 만들다 보면 수많은 에러가 발생함
# 코드를 잘못 작성하거나, 실행상의 문제로 인해
# 에러가 발생하면 프로그램 실행이 중단되기도 함


# 하지만, 프로그램이 중단되는 것을 피하기 위해
# 이러한 에러는 무시하고 넘어가줬으면 하는때도 있음
# 에러에 따른 적절한 처리를 하고 싶을때도 있을 것임

# 파이썬에서는 try-except 구문으로
# 예외처리를 할 수 있음

# error와 except 차이 비교
# 오류 : 프로그램 실행 중 오작동이나 비정상적 종료를
# 유발하게 하는 원인

# 컴파일 오류 : 주로 문법적 오류를 의미 - 개발자가 조치 가능
# 논리 오류 : 실행 가능, 하지만 예상한 결과가 안나오는 오류 - 개발자 조치 가능
# 시스템 오류 : 메모리 초과, 서버 접속 불가능 등의 오류 - 조치 불가
# 실행 오류 : 프로그램 실행 중 발생하는 예외적인 오류 - 개발자 조치 가능
# ex) 어떤 값을 0으로 나누는 경우, 리스트의 인덱스를 잘못 호출하는 경우
# 예외 : 개발자가 완전히 조치할 수 없지만
# 어느정도 수습할 수 있는 수준의 덜 심각한 오류
# 예외처리를 통해 프로그램의 비정상 종료를 막을 수 있음

# 오류 발생 1
print('- 프로그램 시작 -')
print(10/5)
print('- 프로그램 끝 -') # 정상종료

print('- 프로그램 시작 -')
print(10/0)
print('- 프로그램 끝 -') # 정상종료

# 오류 발생 2
print('- 프로그램 시작 -')
num = [1,2,3]
print(num[100])
print('- 프로그램 끝 -') # 정상종료

# 발생한 오류를 예외처리하기
#try:
#    오류가 발생할만한 코드
#except:
#    오류 발생시 처리할 코드
try:
    print(num[100])
except:
    print('list오류!')
print('프로그램 종료')    # 중단되지 않고 끝까지 실행

# 예외처리 7- 에러 메세지 상세 출력:
import sys

num = [1,10,20,50]

try:
    idx = int(input('nums의 index는?'))
    divr = int(input('정수'))
    print(num[idx]/divr)
except:
    extype, exval, trackback = sys.exc_info()
    # 현재 발생한 예외 정보를 tuple로 반환
    print(extype.__name__)  # 예외이름  (매직 키보드)
    print(trackback.tb_frame.f_code.co_filename) # 파일명
    print(trackback.tb_lineno)  # 예외발생 위치
    print(exval.message)    # 예외 메세지

# 예외발생과 상관없이 항상 코드 실행 : finally
# 주로 자원반납과 관련된 코드들에 사용
# try:
#    코드
# except:
#    예외처리
# finally:
# 항상실행될 코드
#
try:
    print('- 프로그램 시작 -')
    print(10 / 0)
except:
    print('오류발생')
finally:
    print('- 프로그램 끝 -')  # 정상종료
