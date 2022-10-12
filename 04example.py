# 1.
print('*   *    **    ****    ****   *   *      /////')
print('*   *   *  *   *   *   *   *  *   *     | o o |')
print('*****  *    *  ****    ****    * *     (|  ^  |)')
print('*   *  ******  *   *   *   *    *       | [_] |')
print('*   *  *    *  *    *  *    *   *        -----')

print('                     +---+')
print('                     |   |')
print('                 +---+---+')
print('                 |   |   |')
print('             +---+---+---+       /\\_/\\     ------')
print('             |   |   |   |      ( \' \' )  / Hello \\')
print('         +---+---+---+---+      (  -  ) <  Junior |')
print('         |   |   |   |   |       | | |   \\ Coder!/')
print('         +---+---+---+---+      (__|__)    ------')

# 2.
soju = ['소주', 3000,2]
chic = ['너나치킨', 12000,1]
money = 50000
reg = '2014. 07. 07 14:35'

print('[음식나라]')
print('------------------')
print(soju[0],'\t',2,'\t',soju[1]*soju[2])
print(chic[0],'\t',1,'\t',chic[1]*chic[2])
print('------------------')
print('과세합계','\t\t',(soju[1]*soju[2]+chic[1]*chic[2])//10*9)
print('부과세','\t\t',(soju[1]*soju[2]+chic[1]*chic[2])//10*1)
print('------------------')
print('총합계','\t\t',(soju[1]*soju[2]+chic[1]*chic[2]))
print('받은금액','\t\t',money)
print('잔돈','\t\t',money-(soju[1]*soju[2]+chic[1]*chic[2]))
print('------------------')
print(reg)

# 3.
# rate1, numberOfWindows

# 4.

# 6.
x = 2.5; y = 1.5; m = 18; n = 4
print(x+n*y-(x+n)*y)
print(m / n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 - (1 - (1 - n)))))

# 7.
print(3 + 4.5 * 2 + 27 / 8)
print((True | False) & (3 < 4) | (5!=7))
print(True | (3 < 5 & 6 >= 2))
print(False == 'A')
print((7 % 4 + 3 - 2 / 6) * 'Z')
print()
print()
# 9.
print(27 / 13 + 4)
print()
print()
print()
print()
print()
print()
# 10.
# 11. 이름과 몸무게, 나이를 변수로 선언하고 자신의 것을 값으로 초기화하는
# 프로그램을 작성하여라 (MyInfo)
name = '홍길동'
weight = 61.5
age = 29
print(name, weight, age)

# 12. 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라. (MyAge)
# 파이썬의 if 단축식 : 참일때값 if 조건식 else 거짓일때 값 elif
myBirth = "941002"
if int(myBirth[:2])<30:
    myAge = 2022 - (1900+int(myBirth[:2])-1)
else:
    myAge = 2022 - (1900+int(myBirth[:2])-1)

print(myAge)


# 13. 구구단 중 7단을 출력하는 프로그램을 작성하여라. (GuGu7Dan)
for i in range(10):
    print('7 * ',i,'=',7*i)

# p57, ex3)

select = 1
main_menu = f'''
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
----------------
=> 작업을 선택하세요.
'''
print('성적 처리 프로그램')
print('----------------')
while select != 0:
 select = input(main_menu)
 if select == 1:
     print('<성적 데이터 추가>')
     name = input('이름을 입력하세요')
     korS = int(input('국어성적을 입력하세요'))
     engS = int(input('영어성적을 입력하세요'))
     mathS = int(input('수학성적을 입력하세요'))
     name_score = [name,korS,engS,mathS]
     print(f'{name:s}님의 성적: 국어-{korS:d} 영어-{engS:d} 수학-{mathS:d}')





