# 컨프리헨션comprehension - 축약표기
# 다양한 데이터 객체에 사용하는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원

# 파이썬에는 4가지 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약
# 1 ~ 10까지의 정수를 생성해서 리스트에 저장
a = list(range(1,10+1))
print(a)

b = []
for i in range(1,10+1):
    b.append(i)
print(b)

# 리스트 for 축약문
# [ 표현식 for 항목 in 반복가능객체 ]
c = [i for i in range(1,10+1)]
print(c)

# 1 ~ 20사이 정수중 짝수를 리스트로 생성
d = [i for i in range(1,20+1) if i % 2 == 0]
print(d)

# ex) 1 ~ 10사이 정수를 제곱한 값을 리스트로 생성
e = [i**2 for i in range(1,10+1)]
print(e)

# ex) 새로운 리스트에 제곱값을 계산하여 생성
f = [1, 2, 3, 4, 5]
f1 = [1, 2, 'A', False, 9, 100]
f = [i**2 for i in f]
f1 = [i**2 for i in f1] # 오류발생

# 변수 유형 확인: type(대상)
print(type(1),type('A'), type(False))

# 조건식을 이용해서 재작성 - 정수일 경우 제곱 연산
k = []
for v in f1:
    if type(v) == int:
        v.append(v**2)
print(k)

k = [v**2 for v in f1 if type(v) == int ]
print(k)

# 1 ~ 60 정수 중 홀수만 골라 리스트에 저장
g = [i for i in range(1,60+1) if i % 2 != 0]
print(g)

# 1 ~ 60 정수 중 5의 배수만 골라 리스트에 저장
h = [i for i in range(1,60+1) if i % 5 == 0]
print(h)

# for 다중 if 축약문
# [ 표현식 for 항목 in 반복가능객체]
# ex) 1 ~ 100 사이 정수 중 임의의 정수가 짝수면 'even'
# 홀수면 'odd' 라고 구분해서 리스트에 저장
l = ['even' if i % 2 == 0 else 'odd' for i in range(1,100+1) ]
print(l)

# 중첩 for 축약
# [표현식 for 항목1 in 반복가능객체1
#   for 항목2 in 반복가능객체2]
# ex) 구구단 중 7, 8단의 결과값을 리스트에 저장
even = [i*j for i in range(7,8+1) for j in range(1,9+1)]
print(even)

# ex) name, grd 리스트의 값들을
# 각각의 키와 값으로 딕셔너리에 저장
name = ['혜교','지현','수지']
grd = ['우','미','수']

# 단순하게 작성
# 새로운 dict요소 생성 : 객체명[키이름] = 값
s = {}
s[name[0]] = grd[0]
s[name[1]] = grd[1]
s[name[2]] = grd[2]
print(s)

# 반복문으로 작성
for i in range(3):
    s[name[i]] = grd[i]
print(s)

# 딕셔너리 for 축약문
# { for k,v in zip(반복가능객체1,반복가능객체2)}
s = {k:v for k,v in zip(name,grd) }
print(s)

# ex) 학생과 국어점수에 대한 리스트가 있을때
# 학생은 키로, 합격여부를 값으로 하는 딕셔너리 객체를 생성
# 단, 합격여부에는 국어점수가 85점이상인 경우 '합격'
# 그외는 '불합격'이라고 출력함
name = ['철수','영희','길동','꺽정']
kor = [50, 80, 90, 60]

result = {n:'합격' if (r >= 85) else '불합격' for n,r in zip(name,kor) }
print(result)

# p111 ex3)
message = ['spam','ham','spam','ham','spam']

# A) spam은 1로 ham은 0으로 생성하는 dummy 변수 생성
dummy = [1 if i=='spam' else 0 for i in message]
print(dummy)

def makeDummy(x):
    val = 0
    if x == 'spam': val = 1
    return val

dummy = list(map(makeDummy, message))
print(dummy)
# B) spam 원소만 추출
spam = ['spam' for i in dummy if i == 1]
print(spam)

def makeSpams(x):
    isSpam = False
    if x == 'spam': isSpam = True
    return isSpam

list(filter(lambda x:x == 'spam',message))