import random as rnd
# p78 숫자맞추기

# 복권 프로그램 = 3 자리 입력
# 난수 범위 - 100 ~ 999
# 3개 일치 - 상급 100만!
# 2개 일치 - 상금 5만!
# 1개 일치 - 상금 1천!
# 0개 일치 - 다음 기회에!

myLotto = input('3자리를 입력하시오.')
result = ['상급 100만원!', '상급 5만원!', '상급 1천원!', '다음 기회에!']

lotto = str(rnd.randint(100,999))
if myLotto[0] in (lotto[0],lotto[1],lotto[2]):
    if myLotto[1] in(lotto[0],lotto[1],lotto[2]):
        if myLotto[2] in (lotto[0], lotto[1], lotto[2]):
            print(result[0],lotto)
        else: print(result[1],lotto)
    else: print(result[2],lotto)
else: print(result[3],lotto)

# 48. 잔액 25,000원 / 금리 6% / 2배가 되려면 몇 년?
stMoney = 25000
its = 0.06
year = 0
mtp = 2
ltMoney = stMoney

while True:
    ltMoney += ltMoney*its
    year += 1
    if ltMoney >= stMoney*mtp:
        break
print(year,'년 뒤 입니다.')

# 51. 반복문 이용하여 테이블 형태 출력
print('\t\t\tMultiplication Table')
print('\t\t1\t2\t3\t4\t5\t6\t7\t8\t9')
print('-----------------------------------------')

for i in range(1,10):
    print(f'{i}\t|\t{i}\t{i*2}\t{i*3}\t{i*4}\t{i*5}\t{i*6}\t{i*7}\t{i*8}\t{i*9}')

# 53. 공식을 이용하여 입력한 년도의 1월 달력 출력
# 0: 일 1: 월 2 : 화 ... 6: 토
year = 2022
mCount = int((((year-1)*365 + (year-1)/4 - (year-1)/100 + (year-1)/400) % 7) + 1 )
print(mCount)   # 2022년 12월 31일의 요일




