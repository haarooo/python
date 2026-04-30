
# numpy : 배열 기반 , 공학 수치 계산
# pandas : 테이블 기반 , 전처리/피터링(numpy)
    # 1차원 : series
    # 2차원 : dataframe

# pandas 설치
# import pandas as pd
import pandas as pd
print(pd.__version__)

# series
# 1. 생성
x = [10,20,30,40] 
z = pd.Series(x)
print(z)

y = ['a','b','c','d']
z = pd.Series(x , index=y)
print(z)

# 딕셔너리로 생성
y = {'apple' : 1 , 'banana' : 2 , 'cherry' : 3}
z = pd.Series(y)
print(z)

# 주요 속성 확인
print(z.dtype)  # 타입반환
print(z.index)  # 인덱스 반환
print(z.values) # 값 반환
print(z.head(2)) # 기본값으로 상위 5개만 출력
print(z.tail(5)) # 하위 n개 출력

print(z.iloc[1]) # iloc[인덱스 번호] , 라벨이 아닌 위치로 조회
print(z.loc['apple'])
print(z.loc['apple':'cherry'])
print(z.iloc[1:3]) # 슬라이싱

# 데이터 수정
z['apple'] = 10
print(z['apple'])

# 데이터 추가
z['berry'] = 40
print(z)

# 병합
x = pd.Series([10,20,30] , index=['a','b','c'])
y = pd.Series([40,50] , index=['d','e'])
z = pd.concat([x,y])
print(z)

# 라벨 이름 변경 , rename({'기존' : '새로운'})
z = z.rename({'a' : 'apple'})
print(z)

# 필터링 
print(z[z>30])
z[z>30] = z[z>30] +10 # 30초과한 요소값에 10 더한 후에 30초과한 요소에만 대입
print(z)

x = z[(z<25) | (z>35)]
print(x)
x = z[(z<25) & (z>35)]
print(x)

# 통계
print(z.sum())
print(z.mean()) # 평균
print(z.max())
print(z.min())
print(z.median()) # 중앙값
print(z.var()) # 분산
print(z.std()) # 표준편차
print(z.count()) # 요소 개수
print(z.value_counts()) # 각 요소별 중복 수
print(z.value_counts(normalize=True)) # 각 요소가 전체에서 차지하는 비율

# 정렬 .sort_index() , .sort_values()
x = z.sort_index()
print(x)
x = z.sort_values()
print(x)

x = z.sort_index(ascending=False) # 내림차순
print(x)

# 그룹
x = z.groupby(level=0).sum()
print(x)
z = pd.Series([10,20,30,10,20,30],index=['a','b','a','b','a','b'])
x = z.groupby(level=0).sum() # 인덱스(라벨)별 총합계
print(x)

x = z.groupby(level=0).mean() # 인덱스별 평균
print(x)

x = z.groupby(level=0).agg(['sum' , 'mean' , 'count']) #여러개 집계함수는 agg함수로 묶어서 표현
print(x)



