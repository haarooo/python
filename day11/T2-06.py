
import numpy as np
# 1차원 배열 통계
x = np.array([1,2,3,4,5])

print(np.min(x))
print(np.max(x))
print(np.argmin(x)) # 최솟값 (인덱스)위치
print(np.argmax(x)) # 최댓값 (인덱스)위치 
print(np.ptp(x)) # 최댓값 - 최솟값
print(np.sum(x)) # 합계
print(np.mean(x)) # 평균
print(np.median(x)) # 중앙값
print(np.var(x)) # 분산
print(np.std(x)) # 표준편차
print(np.sqrt(x)) # 루트

# 사분위수 " 구역을 4개 구역으로 나눠서 데이터 분포 위치 파악
q1 = np.percentile(x , 25) # 1/4 , 하위 25%
q3 = np.percentile(x , 75) # 3/4 , 하위 75%
print(q1)
print(q3)
q2 = np.percentile(x , 50) # 1/2 중앙값 
print(q2)
q3 - q1
print(q1)


# 2차원 배열 통계  , axis = 0(열기준) , 1(행기준)
y = np.array([[1,2,3],[4,5,6]])
print(np.min(y , axis=1))
print(np.min(y , axis=0))
print(np.max(y)) # axis 생략하면 2차원배열 평탄화(1차원으로 변경)
print(np.argmax(y))
print(np.argmin(y))
print(np.sum(y))
print(np.mean(y))
print(np.median(y))
print(np.var(y))
print(np.std(y))

