# 수식 expression
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 => 피연산자와 연산자로 구성
# 연산자: 연산의 의미를 지닌 기호
# 피연산자: 연산의 대상들을 의미

# 대입식: 대입 연산자를 이용한 수식(변수 = 수식)
a = 10; b = 20; c = 30
x,y,z = 10, 20, 30
print(a,b,c,x,y,z)

#산술식: 산술연산자(+,-,*,/) + (//,%,**)
print(10 / 3, 10 % 3, 10 // 3)  # 나누기, 나머지, 몫
print(10**1,10**2,10**3)        # 지수 연산

# 관계식: 관계연산자(대소, 순서관계)를 이용한 수식
print(10 > 3, 10 < 3)

# 논리식: 논리연산자(논리 합/곱/부정)를 이용한 수식
# 논리식의 경우, 수식의 구성에 따라 단축식 평가 short-circuit가 가능
print((5 == 3) and (5 > 3))
print((5 != 3) or (5 > 3))

print("python" and 9>7, 68 and 9>7)
print("python" and 9<7)
print(9>7 or 0, 3 and 9>7)

# 연산자 우선순위
# () > ++,-- > *,+ > and, or > (>,<, ==)

# 연산자의 부수적인 기능 - 문자열 연산
# + : 문자열 연결
# * : 문자열 반복 연결

print(123 + int('456'))
bool(1)