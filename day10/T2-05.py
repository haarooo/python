import numpy as np

# 병합

# .concatenate(x,y),axis = 0) axis = 0(행기준) 1(열기준)
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(np.concatenate((x , y) , axis= 0))
print(np.concatenate((x , y) , axis= 1))

# 정렬
x = np.array([3,1,2,3,4])
print(np.sort(x))
print(np.sort(x)[::-1])

# 2차원 정렬 , .sort(x,axis=0) , axis = 0(열기준) 1(행기준)
x = np.array([[12,1,2] , [9,8,7]])
print(np.sort(x,axis=0))
print(np.sort(x,axis=1)) 
print(np.sort(x,axis=None))

# 2차원 정렬 내림차순 주의할점 : 2차원 슬라이싱 사용 , [행슬라이싱 , 열슬라이싱]
print(np.sort(x,axis= 0)[:,::-1]) # 열 기준 내림차순
print(np.sort(x,axis=-1)[::-1]) # 행 기준 내림차순

# np.sort() vs 배열.sort()
x= np.array([3,2,4])
print(np.sort(x))
print(x.sort())
print(x)

#
x = np.array([20,30,23,24])
y = np.array(['철수' , '영희' , '민수' , '영희'])
z = np.lexsort((x,y))
print(x[z])
print(y[z])


# 필터링
x = np.array([10,20,30,40,50])
print(x >30)
print(x[x>30])

y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y%2==0)
print(y[y%2==0])

# 조건부 필터링
print(np.where(x>30 , x ,0)) # 만약에 요소값이 30보다 크면 그대로 아니면 1
print(np.where(y%3==0 ,y ,1)) # 만약에 요소값이 짝수이면 그대로 아니면 1

# 마스크 필터링
con1 = x>30
print(con1)
z = np.ma.array(x,mask=con1)
print(np.ma.sum(z))

# 다수 조건 필터링
con2 = y%2 == 0  # 조건1 짝수
con3 = y%4 == 0  # 조건2 4배수
print(y[con2&con3])