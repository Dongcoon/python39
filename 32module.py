# 모듈
# 함수나 변수 또는 클래스를 모아 놓은 파일
# 복잡하게 작성한 코드들을 용도에 따라
# 개별 파일에 따로 분리해 둔 것을 의미
# 개발자들끼리 협업시 각자 작성한 코드를
# 모듈로 분리해서 관리하고 이것들을 하나로 통합해서
# 하나의 프로그램으로 만듦

# 모듈 불러오기 : import 모듈명
# 모듈은 보통 파이썬 소스파일에 작성함

import bigdata

# 모듈명.함수명 / 모듈명.변수명 / 무듈명.클래스명
print(bigdata.add(3, 5))
print(bigdata.sub(3, 5))

# 모듈 사용하기 2 - 모듈명 생략
# from 모듈명 import 함수명 (비추)

# from mldl import add,sub
from bigdata import *

print(add(10,5))
print(sub(10,5))

# 모듈 사용하기 4 - 모듈명 생략
# import 모듈명 as 별칭 (추천!)
import bigdata as big
print( big.add(3,5))
print( big.sub(3,5))

# 패키지
# 서로 관련있는 모듈들을 특정 폴더에 모아둔 것
# 모듈 구성시 __init__.py 파일이 필요할 수 있음
# 세분화된 모듈명은 .으로 구분해서 작성
import mldl.math as bdm

print(bdm.mul(3,5))
print(bdm.div(3,5))

# 모듈의 적절한 저장 위치
# 모듈이 적절히 포함되려면
# 실행파일과 같은 공간(디렉토리)에 함께 있어야 함
# 프로젝트내 모듈이 존재한다면 해당 모듈은
# 실행중인 프로젝트만 사용가능 (추천!)
# 모든 프로젝트에서 모듈을 사용하려면
# C:\Users\LG PC\Desktop\Pro\develop_tool\python\Lib 아래에
# 모듈을 저장해두면 됌

# 외부 모듈 사용하기
# 내장 모듈이나 사용자 정의 모듈 이외에
# 다른 조직/기관이나 개인이 만든 모듈을 사용하려면
# 먼저 모듈을 다운로드해서 설치해야만 함
# pip install 모듈명
# pip install sklearn