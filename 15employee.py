# employees.csv를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid
empno = []
fname = []
lname = []
email = []
hdate = []
jobid = []
sal = []
deptid = []
list = [empno,fname,lname,email,hdate,jobid,sal,deptid]
while True:
    print('1. 사원등록\t2. 사원검색\t3. 사원수정\t4. 사원삭제\t5.사원전체출력\t6. 종료')
    sel = int(input('입력 > '))
    if sel == 1:
        empno.append(input('사번을 입력하세요'))
        fname.append(input('이름을 입력하세요'))
        lname.append(input('성을 입력하세요'))
        email.append(input('이메일을 입력하세요'))
        hdate.append(input('입사일을 입력하세요'))
        jobid.append(input('직책을 입력하세요'))
        sal.append(input('급여를 입력하세요'))
        deptid.append(input('부서번호를 입력하세요'))
        print('등록완료!!')
    elif sel == 2:
        select = input('검색할 사번을 입력하세요')
        if select == None:
            print('해당 사번정보가 존재하지 않습니다.')
        else:
            idx = empno.index(select)
            print(f'사원정보: {empno[idx]}\n'
                  f'이름: {fname[idx]}\n'
                  f'성: {lname[idx]}\n'
                  f'이메일: {email[idx]}\n'
                  f'입사일: {hdate[idx]}\n'
                  f'직책: {jobid[idx]}\n'
                  f'부서번호: {deptid[idx]}\n'
                  f'------------------------'
                  f'검색완료!!\n\n')
    elif sel == 3:
        select = input('수정할 사번을 입력하세요')
        if select == None:
            print('해당 사번정보가 존재하지 않습니다.')
        else:
            idx = empno.index(select)
            empno[idx] = input('사번을 입력하세요')
            fname[idx] = input('이름을 입력하세요')
            lname[idx] = input('성을 입력하세요')
            email[idx] = input('이메일을 입력하세요')
            hdate[idx] = input('입사일을 입력하세요')
            jobid[idx] = input('직책을 입력하세요')
            sal[idx] = input('급여를 입력하세요')
            deptid[idx] = input('부서번호를 입력하세요')
            print('수정완료!!')
    elif sel == 4:
        select = input('삭제할 사번을 입력하세요')
        if select == None:
            print('해당 사번정보가 존재하지 않습니다.')
        else:
            idx = empno.index(select)
            for i in range(idx):
               del list[i][idx]
            print('삭제완료!!')
    elif sel == 5:
        print('\t\t\t사원 정보')
        print('사번\t\t 이름\t\t 성\t\t 이메일\t\t 입사일\t\t 직책\t\t 급여\t\t 부서번호')
        print('-----------------------------------------')
        for i in range(len(empno)):
            print('')
            for j in range(len(list)):
                print(list[j][i],'\t\t',end='')

        print('\n------------------출력완료-----------------')
    elif sel == 6:
        check = str(input('종료할까요?(y/n) > '))
        if check in ('y', "Y"):
            print('종료합니다.')
            break
    else:
        print('잘못 입력하였습니다.')
        continue
