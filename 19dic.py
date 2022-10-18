# dict
# 비순차 자료구조
# 키를 통해 값을 찾는 연관배열 객체
# 선언방법은 { 키:값 } 형태로 정의하고 사용
# 다양한 자료형으로 구성된 데이터를
# 하나의 변수로 접근할 수 있음

# dict 선언
member = {'길동': 90, '하나': 80}

# dict 값 출력
for val in member.values():
    print(val, end=' ')

# dict 모든 키, 값 조회: 객체명.item()
print(member.items())
for k, v in member.items():
    print(f'{k}, {v}', end=' ')

# dict 모든 키, 값 조회 2: 키 이용
for k in member.keys():
    print(member[k], end=' ')

# dict 모든 키,값 조회 3: 객체명.get(키) 이용 (추천!)
for k in member.keys():
    print(member.get(k), end=' ')

# dict 동적 생성 1
user = {} # 사용자 - 이름, 나이, 이메일로 구성

# 객체명[새로운키] = 새로운 값
user['name'] = '홍길동'
user['email'] = 'gonga@naver.com'
user['age'] = 29

print(user)

# dict  동적 생성 2: {키:값, ...}
user2 = {'홍':'길동', '강':'동석'}

print(user2)

# dict 동적 생성 3: list 이용 - [[키,값],....]

# dict 수정하기: 객체명[기존키] = 새로운값
user['age'] = 30
user['email'] = 'g@c.m'

# dict 삭제하기 : del 객체명[기존키] - 키와 갑시 모두 삭제
del user['age']

# 객체명.get(키) vs 객체명[키]
user['regdate']    # 존재하지 않느 키 호출시 오류 O

user.get('regdate') # 존재하지 않을 시 오류 X

# 저장형식: { 'name': , 'kor': , 'eng': , 'mat': , 'tot': , 'avg': , 'grd': }
sjs = []

for _ in range(3):
    # 데이터 입력
    name = input('이름: ')
    kor = int(input('국어: '))
    eng = int(input('영어: '))
    mat = int(input('수학: '))

# 성적 처리
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    # 데이터 저장
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

    sjs.append(sj)

# 결과 출력
for sj in sjs:
    print(sj)

# dict 형식 데이터 출력시 예쁘게 표시 : pretty print
from pprint import pprint as pp

pp(sjs)

school = {'혜교': 99, '지현': 65, '수지': 75 }
for student in school.keys():
    print(student,end=' ')
for score in school.values():
    print(score, end=' ')
for key,value in school.items():
    print(key,'의 점수는', value)

# 학생 성적 입력 시스템
import copy
info_temp = {}
info_save = {}

print('1. 학생등록\t2. 학생검색\t3. 학생수정\t4. 학생삭제\t5.학생전체출력\t6. 종료')
while True:
    sel = int(input('입력>'))
    if sel == 1:
        stuNum = input('학번: ')
        stuName = input('이름: ')
        info_temp['학번'] = stuNum
        info_temp['이름'] = stuName
        info_save[stuNum] = copy.deepcopy(info_temp)
        info_temp.clear()
        print('등록완료!!\n')
    elif sel == 2:
        stuNum = input('검색할 학번: ')
        if info_save.get(stuNum) == None:
            print('찾으시는 학번은 존재하지 않습니다.')
        else:
            print(info_save[stuNum],'\n')
    elif sel == 3:
        stuNum = input('수정할 학번: ')
        if info_save.get(stuNum) == None:
            print('찾으시는 학번은 존재하지 않습니다.')
        else:
            newName = input('새로운 이름입력: ')
            info_temp['학번'] = stuNum
            info_temp['이름'] = newName
            info_save[stuNum] = copy.deepcopy(info_temp)
            info_temp.clear()
    elif sel == 4:
        stuNum = input('삭제할 학번: ')
        if info_save.get(stuNum) == None:
            print('찾으시는 학번은 존재하지 않습니다.')
        else:
            print(info_save[stuNum])
            check = str(input('진짜로 삭제할까요?(y/n) > '))
            if check in('y','Y'):
                info_save.pop(stuNum)
                print('삭제 완료!!')
            else: continue
    elif sel == 5:
        for stuNum,stuName in info_save.items():
            print(stuNum,'|',stuName)
    elif sel == 6:
        check = str(input('종료할까요?(y/n) > '))
        if check in('y',"Y"):
            print('종료합니다.')
            break
    else:
        print('잘못 입력하였습니다.')
        continue
