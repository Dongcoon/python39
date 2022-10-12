name = '홍길동'
age = 19
hometn = 'seoul'
print('이름 : %s | 나이 : %d | 주거지 : %s' %(name,age,hometn))

# 출력 - 인덱스, 출력서식 사용 : .format함수 사용
# print({인덱스:출력서식}.format(변수들...))
print('이름: {0:s}'.format(name))
print('이름 : {0:s} | 나이 : {1:d} | 주거지 : {2:s}'.format(name,age,hometn)) #인덱스 생략 가능

# 출력 - 문자열 템플릿(f-string) : py 3.6이후 지원
# print(f'{변수명:출력서식}')
print(f'이름: {name:s}',f'나이: {age:d}',f'주거지: {hometn:s}')
print(f'나이: {age:d}')
print(f'주거지: {hometn:s}')

a = 'a'
b = 1
c = 0.22
d = 'abc'
# %서식
print('a: %c, b: %d, c: %0.3f, d: %s' %(a,b,c,d))

# .format
print('a: {0:s}, b: {1:d}, c: {2:0.2f}, d: {3:s}'.format(a,b,c,d))

# f-string
print(f'a: {a:s}',f'b: {b:d}',f'c: {c:0.2f}',f'd: {d:s}')
