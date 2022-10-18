# employees.csv를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid
name = []
math = []
kor = []
eng = []
sci1 = []
sci2 = []
frl = []
list = [name,math,kor,eng,sci1,sci2,frl]
lstName = ['이름', '수학성적', '언어성적', '영어성적', '생물1 성적','생물2 성적','제2외국어 성적']
while True:
    print('1. 성적등록\t2. 성적검색\t3. 성적수정\t4. 성적삭제\t5.성적전체출력\t6. 종료')
    sel = int(input('입력 > '))
    if sel == 1:
        for i in range(len(list)):
                list[i].append(input(f'{lstName[i]} 입력 > '))
        print('등록완료!!')
    elif sel == 2:
        select = input('검색할 학생이름을 입력하세요')
        if select == None:
            print('해당 학생이 존재하지 않습니다.')
        else:
            idx = name.index(select)
            for i in range(len(list)):
                print(f'{lstName[i]}: {list[i][idx]}점')
            print('검색완료!!')
    elif sel == 3:
        select = input('수정할 학생이름을 입력하세요')
        if select == None:
            print('해당 학생이 존재하지 않습니다.')
        else:
            idx = name.index(select)
            for i in range(1,len(list)):
               list[i][idx] = input(f'{lstName[i]} 입력 > ')
            print('수정완료!!')
    elif sel == 4:
        select = input('삭제할 학생이름을 입력하세요')
        if select == None:
            print('해당 학생이 존재하지 않습니다.')
        else:
            idx = name.index(select)
            for i in range(len(list)):
               list[i].pop(idx)
            print('삭제완료!!')
    elif sel == 5:
        print('---------------학생 성적 정보-----------------------')
        print('이름\t\t수학\t\t언어\t\t영어\t\t생1\t\t생2\t\t제2외국어')
        print('---------------------------------------------------')
        for i in range(len(name)):
            for j in range(len(list)):
                print(list[j][i],'\t\t',end='')
            print()
        print('\n------------------출력완료-----------------')
    elif sel == 6:
        check = str(input('종료할까요?(y/n) > '))
        if check in ('y', "Y"):
            print('종료합니다.')
            break
    else:
        print('잘못 입력하였습니다.')
        continue

print(name)