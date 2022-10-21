# 파일 입출력
# 지금까지 값을 입력받을때는
# 사용자가 직접 키보드로 입력하는 방식을 사용했고
# 값을 출력할때는 모니터 화면에 표시하는 방식을 사용했음

# 하지만, 값을 입력받거나 출력하는 방법은 이게 다가 아님
# 파일을 통해 값을 입력/출력할 수 있고
# 네트워크를 통해 값을 입력/출력할 수도 있음

# 프로그램 실행 중 생성된 데이터(변수)들은
# 주로 메모리 내에 존재하는데 프로그램 종료시 같이 소멸됨(휘발성)
# 데이터의 영속성persistence을 부여하기 위해서는
# 데이터를 저장장치에 보관해서
# 데이터가 소멸되지 않도록 하는 것이 중요!

# 파일쓰기 : 데이터를 파일에 기록
# 파일객체변수 = open(경로, 모드)        # py2
# with open(경로, 모드) as 파일객체변수  # py3

# 파일모드 : 파일작업 종류
# w(쓰기), a(추가쓰기), t(텍스트파일 쓰기),
# b(바이너리파일 쓰기)

# 파일쓰기 작업이 끝나면 반드시 close 해줘야 함
# 단, with문을 사용하는 경우 close 생략 가능

# 간단한 인삿말을 파일에 저장

# py2
# open(경로/파일명, 작업모드)
f = open('hello.dat','w')   # 쓰기모드로 파일생성
f.write('Hello, World!!')   # 지정한 파일에 내용쓰기
f.close()                   # 작업종료시 파일 닫음

# open(경로/파일명, 작업모드, 인코딩) as 별칭
# py3
with open('hello2.dat', 'w', encoding='UTF-8') as f:
    f.write('안녕, 세상아!!')

# 회원정보를 입력받아 member.dat에 저장
# 저장대상 : 아이디, 비밀번호, 이름, 이메일
# 저장형식 : "아이디/비밀번호/이름/이메일" 형식으로 파일에 저장
# ex) abc123/987xyz/홍길동/abc123@nave.com
with open('member.dat','w',encoding='UTF-8') as f:
    userid = input('아이디 입력 >')
    passwd = input('비밀번호 입력 >')
    name = input('이름 입력 >')
    email = input('이메일 입력 >')
    data = f'{userid}/{passwd}/{name}/{email}\n'
    f.write(data)

# 파일에 데이터 누적시켜 저장하기
# 파일쓰기모드를 a라고 지정하면
# 이전에 저장한 내용에 새로운 내용을 추가해서 저장함
with open('member.dat','a',encoding='UTF-8') as f:
    f.write(data + '\n')

# 학생으로부터 이름,국어,영어,수학 점수를 입력받아
# 파일에 저장하세요 (파일명 : sungjuk.dat)
# 단, 점수는 임의로, 파일에 저장하는 형식은
# "이름,국어,영어,수학" 순으로 작성함
# => 혜교,99,98,99
with open('sungjuk.dat','w',encoding='UTF-8') as f:
    name = input('이름 입력 >')
    kor = input('국어성적 입력 >')
    eng = input('영어성적 입력 >')
    mat = input('수학성적 입력 >')
    data = f'{name},{kor},{eng},{mat}'
    f.write(data)

# 파일읽기 : 파일 내 데이터 읽어오기
# 파일객체변수 = open(경로, 모드)        # py2
# with open(경로, 모드) as 파일객체변수  # py3

# 파일모드 : 파일작업 종류
# r(읽기, 생략가능), t(텍스트파일 읽기), b(바이너리파일 읽기)

# 파일읽을때 사용가능 함수
# read    : 텍스트파일의 내용을 모두 읽음
# readline : 텍스트파일의 내용을 한줄씩 읽어옴 (반복문사용)
# readlines : 텍스트파일의 내용을 한줄씩 모두 읽어옴

# 간단한 인삿말을 파일에서 읽어오기
f = open('hello.dat')
doc = f.read()  # 파일내용을 모두 읽어 문자열로 저장
f.close()
print(doc)

with open('hello.dat') as f:
    doc2 = f.read()
print(doc2)

# 인삿말이 저장된 hello2.dat 파일에서도 읽어오기1
with open('hello2.dat',encoding='UTF=8') as f:
    doc2 = f.read()
print(doc2)

# 여러건의 회원정보가 저장된 파일 읽어오기 2
with open('hello2.dat',encoding='UTF=8') as f:
    doc3 = f.readlines()    # 행 단위로 읽어 리스트에 반환
print(doc3)

for doc in doc3:
    print(doc,end=' ')

# 여러건의 회원정보가 저장된 파일 읽어오기 3
with open('hello2.dat',encoding='UTF=8') as f:
    doc4 = f.readline()    # 행 단위로 읽어 하나씩 읽어 반환
print(doc4) # 한건만 출력됨

# 여러건의 회원정보가 저장된 파일 읽어오기 4
with open('hello2.dat',encoding='UTF=8') as f:
    doc5 = []
    while True:
        line = f.readline()     # 파일로부터 한줄 읽어서
        if not line: break     # 읽은 내용이 없으면 반복 중지
        doc5.append(line)       # 읽은 내용이 있다면 리스트에 저장

print(doc5)

# 여러건의 회원정보가 저장된 파일 읽어오기 5
with open('sungjuk.dat',encoding='UTF=8') as f:
    while True:
        line = f.readline()
        if not line: break
        item = line.split(',')  # 각 행의 자료를 구분자로 분리해서
                                # 리스트로 저장
        out = f'{item[0]} {item[1]} {item[2]} {item[3]}'
        print(out, end=' ')

# 앞 예제에서 파일로저장한 성적데이터를
# 다음과 같은 형태로 화면에 출력
# 이름 : abc, 국어 : 99, 영어 : 87, 수학: 66
