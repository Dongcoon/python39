#for 반복변수 in range(시작값, 종료값-1, 증감값):

# range함수 사용하기
list(range(10)) # 0~(10-1) 범위

# 1~100 사이 정수 출력
for i in range(1,100):
    print(i,' ',end="")

# 1~100 사이 정수 중 짝수만 출력
for i in range(2,100,2):
    print(i,' ',end="")
for i in range(1,100):
    if i % 2 == 0: print(i,' ',end="")

# n의 약수 구하기
n = 100
for i in range(1,n+1):
    if n % i == 0: print(i,end=" ")

# 1~100사이 정수 합계 출력
# ((x+y) * (y - x + 1)) / 2
sum = 0
for i in range(31,102):
    sum += i
print(sum)

print((31+101)*35.5)

# 문자열에 반복문 적용하기
# => 문자열에서 문자를 하나씩 가져와서 출력함
for i in 'Hello World!!':
    print(i, end=' ')

# 구구단
n = int(input('몇단? '))
for i in range(1,10): print(f'{n:d} * {i:d} = {n*i:d}',end=' ')

# 3의 배수이지만 2의 배수는 아닌 정수 출력
sum = 0
result = ''
for i in range(1,100):
    if i % 3 == 0 and i % 2 != 0:
            sum += i
            result += str(i) + " "
print(sum)
print(result)
