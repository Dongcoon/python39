# input 함수
# 변수명 = input(입력메세지)

#성적처리 프로그램 v2
sc1 = input()
print(sc1)

name = input('이름을 입력하시오')
korS = int(input('국어성적을 입력하시오'))
engS = int(input('영어성적을 입력하시오'))
mathS = int(input('수학성적을 입력하시오'))
print(f'이름: {name:s}', f'국어성적: {korS:d}',f'영어성적: {engS:d}',f'수학성적: {mathS:d}')
sum = korS+engS+mathS
avg = sum/3
print(f'합산: {sum:d}',f'평균: {avg:0.2f}')