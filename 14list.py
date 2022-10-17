# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

list = []

# insert(인덱스: 값) : 인덱스에 값이 존재하면 그 값은 뒤로 밀림
# append(값) : 맨 뒤에 값 추가
list.append('라면')
list.append('돈까스')
list.insert(1,'짜장면')      # ['라면','짜장면','돈까스']
print(list)

# list.pop(값) : 맨 뒤에 부터 출력 후 값 삭제
list.pop()
print(list)

# 다양한 데이터 다루기
datas = []
datas.append(1)
datas.append(2.5)
datas.append(True)
datas.append('Hello')
datas.append([1,2,3,4])
print(datas)


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
