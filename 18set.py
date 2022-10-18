# 집합(set)
# 비순차 열거형 자료구조
# 데이터가 저장된 순서를 기억하지 않음 (인덱스 사용x)
# 단, 집합을 리스트나 튜플로 변환하면 사용가능
# 입력된 데이터의 중복을 허용하지 않음
# 선언방법은 값들을 {}안에 정의하고 사용

# 집합 선언

nums = {1,2,3,4,5}

# 집합 출력 1
nums[0] # 인덱스를 이용한 조회 불가

# 집합 출력 2
for i in range(len(nums)): # 순차 조회 불가
    print(nums[i])

# 집합 출력 3
for num in nums:
    print(num,end=' ')

# 집합 값 제거: remove(값)
nums.remove(20)
print(nums)

# 집합 값 수정 : 기본적으로는 불가, 단 리스트 변환시 가능
nums[0] = 999
nums = list(nums)
nums[0] = 999
nums = set(nums)

print(nums)

import random as rnd
# ex) 로또 645 : 1~45사이 임의의 숫자 6개 생성
# 단, set을 이용해서 같은 숫자가 출현하지 않도록 작성
ltoList = set()
while len(ltoList) != 6:
    ltoList.add(rnd.randint(1,45))
print(ltoList)

# ex) 로또 645 : 1~45사이 임의의 숫자 6개 생성
# 단, list을 이용해서 같은 숫자가 출현하지 않도록 작성
ltoList = []
while len(ltoList) != 6:
    num = rnd.randint(1,45)
    if num in ltoList:
        continue
    else:
        ltoList.append(num)
print(ltoList)
