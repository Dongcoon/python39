# 함수function
# 주어진 입력값으로 무언가를 수행하고 결과물을 내놓는 객체
# 한번 작성해두면 언제든 재사용 가능
# 논리적인 단위 분할 가능 -> 개발의 분업화
# 코드의 구현을 외부로 부터 숨길수 있음 -> 캡슐화

# 함수 정의
# def 함수이름(매개변수):
#     함수몸체

# 함수 호출
# 함수이름(인수)

# 인사말 출력하는 코드 1
print('Hello, World!!')

# 인사말 출력하는 코드 2 - 3번 반복
for _ in range(3):
    print('Hello, World!!')

# 인사말 출력하는 코드 3 - 3번 반복을 3번 반복
# 복붙으로 해결 할 수 있지만, 수정사항이 생기면 유지보수가 어려움
for _ in range(3):
    print('Hello, World!!')
for _ in range(3):
    print('Hello, World!!')
for _ in range(3):
    print('Hello, World!!')

for _ in range(3):
    for _ in range(3):
        print('Hello, World!!')

# 인사말 출력하는 코드 4 - 함수 이용
def sayHello():     # 함수 정의
    for _ in range(3):
        for _ in range(3):
            print('Hello, World!!')

def sayHello(msg):     # 함수 정의
    for _ in range(3):
        for _ in range(3):
            print(f'Hello, {msg}!!')

# sayHello()   >>   오버로딩 공식지원은 X - 구현가능
sayHello('파이썬')
sayHello(33)

# 두 수를 입력받아 add라는 합수로 호출해서 결과 출력
def add(a,b):
    print('a+b = ',a+b)

add(224,999)

