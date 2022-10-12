import random
# ex) 주민번호에서 생년월, 일 성별을 추출해서 변수에 저장
error = 0

while (error==0):
    jumin = input('@@@@@@-@@@@@@@')
    if 100>int(jumin[:2])>20:
        year = 1900+int(jumin[:2])
    elif 0<int(jumin[:2])<=20:
        year = 2000 + int(jumin[:2])
    else:
        print('년도가 잘못되었습니다.')
        continue

    if (int(jumin[2:4])!=0)&(int(jumin[4:6])!=0):
        birth = jumin[2:4] + '월' + jumin[4:6] + '일'
    else:
        print('생년월일이 잘못되었습니다.')
        continue

    if (jumin[7]=='1')|(jumin[7]=='3'):
        sx = 'male'
    elif (jumin[7]=='2')|(jumin[7]=='4'):
        sx = 'female'
    else:
        print('성별 번호가 잘못되었습니다.')
        continue
    error = 1
    print(year, birth, sx)

# 잔돈계산
#비용과 지불금액을 입력받아 잔돈 계산

payM = int(input('상품금액:'))
recM = int(input('받은금액'))
remM = recM - payM

print(f'상품금액: {payM:d}원, 받은금액: {recM:d}원, 잔액: {remM:d}원')

m_50000 = remM // 50000
m_10000 = (remM%50000) // 10000
m_5000 = (remM%10000) // 5000
m_1000 = (remM%5000) // 1000
m_500 = (remM%1000) // 500
m_100 = (remM%500) // 100

print(f'5만원: {m_50000:d}장 \n'
      f'1만원: {m_10000:d}장\n'
      f'5천원: {m_5000:d}장\n'
      f'1천원: {m_1000:d}장\n'
      f'5백원: {m_500:d}장\n'
      f'1백원: {m_100:d}장\n')

# ex2) 점수 3개 입력받아 평균 60점 이상, 각 과목 40점이하 과락
scoreA = int(input('과목1'))
scoreB = int(input('과목2'))
scoreC = int(input('과목3'))
avg = (scoreA+scoreB+scoreC)/3

if (scoreA>=40)&(scoreB>=40)&(scoreC>=40):
    print('과락 과목은 없습니다.')
    if avg>=60:
        print(f'과목1:{scoreA:d},과목2:{scoreB:d},과목3:{scoreC:d},과목평균:{avg:0.f}')
        print('최종합격입니다.')
else:
    print(f'과목1:{scoreA:d},과목2:{scoreB:d},과목3:{scoreC:d},과목평균:{avg:d}')
    print('과락 과목이 존재합니다\n'
          '불합격입니다ㅜ')

# 25. 복권 발행
myLotto = ['','','']
lotto = ['','','']
myLotto[0] = input('첫번째 로또번호')
myLotto[1] = input('두번째 로또번호')
myLotto[2] = input('세번째 로또번호')

for i in range(3):
    lotto[i] = str(random.randint(0, 9))
if(myLotto[0]==lotto[0])&(myLotto[1]==lotto[1])&(myLotto[2]==lotto[2]):
    print('축하합니다 당첨입니다!')
else:
    print('아쉽지만 다음기회를~!')

print('내 로또번호 :',myLotto[0],myLotto[1],myLotto[2])
print('당첨번호 :',lotto[0],lotto[1],lotto[2])

# 혼인여부에 따른 납세율 변동
tax = 0
isMarried = True
salary = 7000

if isMarried==False:
    if salary>=3000:
        tax=salary*0.25
        print(f'납부할 세금은: {tax:0.1f} 입니다')
    elif 0<salary<3000:
        tax=salary*0.10
        print(f'납부할 세금은: {tax:0.1f} 입니다')
    else:
        print('납부할 세금이 없습니다.')
else:
    if salary>=6000:
        tax=salary*0.35
        print(f'납부할 세금은: {tax:0.1f} 입니다')
    elif 0<salary<6000:
        tax=salary*0.10
        print(f'납부할 세금은: {tax:1.f} 입니다')
    else:
        print('납부할 세금이 없습니다.')

# 현재 연도에서 윤년의 여부

