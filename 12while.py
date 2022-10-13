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