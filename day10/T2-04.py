
import numpy as np

# 리스트
print([1,2,3]+[4,5,6])

# 배열 연산 , 두 배열간의 동일한 위치끼리 연산 수행
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**2)
print(y//x)

# 비교 연산 
print(x > y)
print(x==y)

# 배열
print(x+20)
print(y*2)

# 논리 연산 , logical_and(x,y)
x = np.array([True , False , True])
y = np.array([False , False , True])
print(np.logical_and(x,y)) # 모두 참이면 참
print(np.logical_or(x,y)) # 하나라도 참이면 참
print(np.logical_not(x,y)) # 반대 

# 루트 , sqrt
y = np.array([1,4,9])
print(np.sqrt(y))

# 2차원 비교
y = np.array([[1,2,3],[4,20,6]])
print(y>3)

x = np.array([1,10,3])
print(x > y)

# .all(x) : 모두 참이면 참 , .any(x) : 하나라도 참이면 참
x = np.array([True, False , True]) 
print(np.all(x))
print(np.any(x))

# .equal(x,y) : 두 배열의 요소들이 모두 같으면 True
x = np.array([1,2,3])
y = np.array([1,2,3])
z = np.array([1,2,4])

print(np.array_equal(x,y))
print(np.array_equal(x,z))