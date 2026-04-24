# 모듈 호출하기
# 표준 모듈 : 파이썬 내장 라이브러리
# 외부 모듈 : 설치형 라이브러리 
# import 모듈명
# from 모듈 import 가져오고 싶은 함수 또는 변수
# 식별자부여 import 모듈명 as 시별자명
import math 
print(math.sin(1))
print(math.cos(2))
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))

from math import sin , cos , tan

import math as m
print(m.sin(1))

# random 모듈
import random 

print(random.random()) # 0.o ~ 1.0 사이의 난수 생성
print(random.uniform(10,20)) # uniform(시작값 , 끝값)
print(random.randrange(10)) # 0 ~ 10 사이 생성
print(random.choice([10,24,5,20])) # choice([리스트]) , 리스트내 랜덤 요소 1개 반환
print(random.shuffle([1,2,3,4,5])) # shuffle([리스트]) , 리스트내 요소들 섞기 , 원본이 수정된다
print(random.sample([1,2,3,4,5] ,k=2)) # 리스트내 k개 랜덤 요소 변환
# k=2 : 키워드 매개변수 , k 라는 이름 갖는 매개변수에 대입 