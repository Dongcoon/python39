# if~else만으로 다양한 조건을 판단하기 어려움
# 다양한 조건에 따라 판단하기 위해서는
# if ~ elif ~ else 구문을 사용해야 함

# if 조건식1:
#    조건식1이 참일때 실행할 문장
# elif 조건식2:
#    조건식2이 참일때 실행할 문장
# ...
# else:
#    거짓일때 실행할 문장

score = 55
if 50 >score >= 0:
    print(f'좀더 분발하세요!')
elif 50 <= score < 80:
    print(f'잘했어요!')
else:
    print('최고에요!')

# 성적
print('성적 처리 프로그램')
print('----------------')
print('<성적 데이터 추가>')
name = input('이름을 입력하세요')
korS = int(input('국어성적을 입력하세요'))
engS = int(input('영어성적을 입력하세요'))
mathS = int(input('수학성적을 입력하세요'))

tot = (korS+engS+mathS)
score = tot/3

if 50.0 > score >= 0.0:
    print(f'평균 점수: {score:.1f} 가!')
elif 50.0 <= score < 60.0:
    print(f'평균 점수: {score:.1f} 양!')
elif 60.0 <= score < 70.0:
    print(f'평균 점수: {score:.1f} 미!')
elif 70.0 <= score < 90.0:
    print(f'평균 점수: {score:.1f}우!')
else:
    print(f'평균 점수: {score:.1f}수!')

result = print(f'{name:s}님의 성적: 국어-{korS:d} 영어-{engS:d} 수학-{mathS:d}')

# 출생년도 입력받아 나이에 따른 학생 분류
print('<나이별 학생 분류>')
birth = int(input('출생년도 입력: ex)1994'))
age = 2022 - (birth-1)


if 14 > age >= 8:
    grade = '초등학생'
    print(f' {age:d} 살은 {grade:s} 입니다!')
elif 14 <= age < 17:
    grade = '중학생'
    print(f' {age:d} 살은 {grade:s} 입니다!')
elif 17 <= age < 20:
    grade = '고등학생'
    print(f' {age:d} 살은 {grade:s} 입니다!')
elif 20 <= age < 26:
    grade = '대학생'
    print(f' {age:d} 살은 {grade:s} 입니다!')
else:
    grade = '성인'
    print(f' {age:d} 살은 {grade:s} 입니다!')

# 신용카드 판별
card = input('신용카드번호는?')
result = ''

if card[:2] == '35':
    nums = card[2:] #나머지 카드 번호 추출
    if nums == '6317': result = 'NH농협 JCB카드'
    elif nums == '6901': result = '신한 JCB카드'
    elif nums == '6912': result = 'KB국민 JCB카드'
    else:  result = '잘못된 카드번호입니다!!'
elif card[:1] == '4':
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '04825':
        result = '비씨 비자카드'
    elif nums == '38676':
        result = '신한 비자카드'
    elif nums == '57973':
        result = '국민 비자카드'
    else:
        result = '잘못된 카드번호입니다!!'
elif card[:1] == '5':
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '15594':
        result = '신한 마스타카드'
    elif nums == '24353':
        result = '외환 마스타카드'
    elif nums == '40926':
        result = '국민 마스타카드'
    else:
        result = '잘못된 카드번호입니다!!'
else:
    result = '잘못된 카드번호입니다!!'
print(result)

# 시간 분류
daytime = 'go'
while daytime != 'break':
    daytime = input('''
    while 
    다음 중 알고자하는 상세시간의 단어를 입력하시오.
    1. morning                 
    2. midday / noon                
    3. afternoon         
    4. evening                  
    5. night                  
    6. midnight                  
    7. early morning          
    8. small                 
    9. dawn / daybreak 
    0. break        
                    ''')
    if daytime =='morning': desc = '아침시간 (7-12)'
    elif daytime in ('midday','noon'): desc = '점심시간 (12-13)' # in 사용.
    elif (daytime =='afternoon'): desc = '오후 (13-18)'
    elif (daytime =='evening'): desc = '저녁시간 (18-21)'
    elif (daytime =='night'): desc = '밤시간 (21-00)'
    elif (daytime =='midnight'): desc = '자정시간 (00시)'
    elif (daytime =='early morning')|(daytime =='earlymorning'): desc = '새벽시간 (00-05)'
    elif (daytime =='small'): desc = '새벽 (01-03)'
    elif (daytime =='dawn')|(daytime =='daybreak'): desc = '해뜰력 (05-07)'
    elif (daytime =='break'): desc = '종료합니다.'
    else: desc ='단어를 잘못 입력하였습니다.'

    print(desc)

# switch ~ case 와 비슷하게 작성해보기
# dict 사용 / v3.10 이상부터 match case 라는 구문으로 구현가능

# dict 자료구조 - 연관 배열 자료형
# 키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류임
# 객체명 = {키 : 값} => 객체명.get(키) or 객체명[키]
cards = {'356317': 'NH농협카드',
        '404825':'비씨Visa카드'}
cards.get('404825')

# 성적 분류 프로그램 dict버전
print('성적 처리 프로그램')
print('----------------')
print('<성적 데이터 추가>')
name = input('이름을 입력하세요')
korS = int(input('국어성적을 입력하세요'))
engS = int(input('영어성적을 입력하세요'))
mathS = int(input('수학성적을 입력하세요'))

tot = (korS+engS+mathS)
score = tot/3

grds = { 10:'수',9:'수',8:'우',7:'미',6:'양', 5:'가',}
grd = grds.get(avg // 10)

# 3항 연산자 - if 단축문 : 컴프리헨션
# 참값 값 if 조건식 else 거짓값
print('참' if False else '거짓')

# 3항 연산 활용 윤년 여부 / 마지막일수 출력
# 30: 4,6,9,11
# 31: 1,3,5,8,10,12
# 28: 2(윤년X)
# 29: 2(윤년O)
start = 0
while start != 1 :
    put = input('년월 - ex)202202')
    year = int(put[:4])
    month = int(put[5:])
    checkY = (year%4==0 and year%100!=0) or year%400==0

    yearC = '올해는 윤년입니다' if (checkY)  else '올해는 윤년이 아닙니다.'
    if month in (4,6,9,11): checkM = 30
    elif month in (1,3,5,8,10,12): checkM = 31
    elif month == 2: checkM =(29 if checkY else 28)
    else: start = 1

    a = f'{yearC:s} 또한 올해 {month:d}월은 {checkM:d}일까지 있습니다.'
    b = '존재하지 않는 월 입니다.'

    print(a if start!=1 else b)

