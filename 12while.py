# while을 이용한 반복문
i = 1
while i<= 100:
    print(i, end=' ')
    i += 1 # ++i 불가능

# 1 ~ 100 사이 정수 중 홀수만 출력
i = 1
sum = ''
while i <= 100:
    if i % 2 == 1: sum += str(i) + ' '
    i += 1
print(sum)

# 무한루프
# 반복문의 조건식이 언제나 참이면
# 반복을 중단하지 않고 계속 반복을 지속하는 상황
# 단, 무한루프에서 탈출하려면 break를 이용
# while True:
#    반복실행할 문장
#  반복실행 중지 : break
i = 1
sum = ''
while True:
    if i <= 100 : sum += str(i) + ' '
    else: break
    i += 1
print(sum)

# 1 ~ 1000사이의 모든 정수의 합
# 단, 누적합 15000넘으면 중지
i = 1
sum = 0
while True:
    if i < 1000 and sum < 15000: sum += i
    else: break
print(sum)

# 반복실행시 특정코드 회피 : continue
# 반복 실행을 유지하면서
# 특정 코드블럭의 실행을 생략하고 싶을 때 사용.

# ex) 1~1000 사이의 모든 정수의 합을 출력하세요.
# 단, 7의 배수나 9의 배수는 제외하고 누적합을 구함
i = 0
hap = 0

while i <= 1000:
    i += 1
    if i % 7 == 0 or i % 9 == 0: continue
    hap += 1    # 상황에 따라 실행될수도, 실행되지 않을 수도 있음.
print(hap)

# 아이디, 비밀번호를 입력받아
# 미리 설정해둔 아이디, 비밀번호 일치하면 '로그인 성공!'
# 일치하지 않으면 '로그인 실패!' 라고 출력하는 조건문 작성
# 아이디: abc123, 비밀번호 : 987xyz
while True:
    id = input('아이디를 입력하시오')
    passwd = input('비밀번를 입력하시오')
    if id == 'abc123' and passwd == '987xyz': break
    else: print('입력정보가 일치하지 않습니다.')

# 난수 생성하기
# 파이썬에서 난수를 생성하려면 random 패키지 이용
# 생성방법: 피키지명.random.ranint(시작값, 끝값)
import random as rnd    # 별칭으로 패키지명 줄여서 씀
rnd.seed(2210171044)    # 난수생성 초기값 지정
print(rnd.randint(1, 10))

for _ in range(6):      # 반복실행 시 인덱스가 필요없으면 _ 사용
    print(rnd.randint(1,45), end=' ')