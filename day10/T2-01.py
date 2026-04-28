
# T2-01.py
# 1. numpy란? 고성능 수치 계산 라이브러리
# 2. 설치 : 터미널에서 pip install numpy
# numpy 불러오기 : import.numpy
import numpy
print(numpy.__version__)

# 넘파이 배열 생성

x = [1,2,3,4] # 일반 리스트
print(x)

x = numpy.array([1,2,3,4]) # .array(자료) 
print(x)

x = numpy.array([[1,2,3],[4,5,6]]) # 2차원 배열
print(x)

x = numpy.zeros((2,3)) # .zeros((행,열)) , 행 과 열 만큼의 0으로 초기화
print(x)

x = numpy.ones((2,3)) # .ones((행 , 열)) , 행 과 열 만큼의 1로 배열 초기화
print(x)

x = numpy.full((2,3),10) # .full((행,열),값) 행과 열 만큼의 값으로 배열 초기화
print(x)

x = numpy.arange(0,10,2) # arange(시작 , 끝 , 단위) # 시박부터 끝 사이의 단위로 구성한 배열
print(x)

numpy.linspace(0,1,5) # .linespace(시작 , 끝 , 개수) # 시작부터 끝 사이의 개수만큼 균등하게 나눈 배열
print(x)

import numpy as np

# .shape 현재 배열의 크기 반환(튜플) , (행개수 , 열개수)
x = np.array([[1,2,3],[4,5,6]]) 
print(x.shape)

# .dtype , 현재 배열내 데이터 타입 반환
x = np.array([1.0,2.0,3.0])
print(x.dtype)

# .size , 현재 배열내 모든 요소 수  
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x.size)

# .ndim , 현재 배열 차원
x = np.array([1,2,3])
print(x.ndim)
x = np.array([[[1],[2]],[[3],[4]]])
print(x.ndim)

# .flat , 다차원 배열을 1차원으로 반환
x= np.array([[1,2],[3,4]])
for element in x.flat:
    print(element)


# 배열의 데이터 타입
# bit란 0또는 1로 이루어진 2진수
# 8bit란 0또는 1로 이루어진 2진수가 8개 모이면 -> 1byte
# 즉 bit많을수록 더 많은 자료 표현할 수 있다


# .array(자료, dtype = numpy.타입명)
x = np.array([1,2,3] , dtype=np.int64) # int32 , 정수형 32bit , bit가 클수록 더 많은 정보를 저장한다
print(x) # 필요에 따라 적절하게 bit 선택
x= np.array([1.0,2.0,3.0] , dtype=np.float64) 
print(x) # float64 , 더 큰 bit이면 더 정밀한 오차를 최소화한다

x = np.array([True , False , True] , dtype=np.bool_)
print(x)

x = np.array(['apple' , 'banana' , 'cherry'] , dtype=np.bytes_)
print(x.dtype) # 문자열을 바이트 형태로 저장

# .astype(numpy.변환타입명) , 타입변환
x = np.array([1.3,2.1,3.3])
y = x.astype(np.int32)
print(y.dtype)


