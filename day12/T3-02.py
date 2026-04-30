
import pandas as pd

pd.Series # 1차원
pd.DataFrame # 2ckdnjs

# 데이터프레임 생성
data_list = [['and' , 25 , 'seoul'],['bee',30,'busan'] , ['cat' , 36, 'incheon']]
x = pd.DataFrame(data_list , columns=['name' , 'age' , 'city'])
print(x)    

# 데이터프래임 생성2 , 대부분의 공공자료는 딕셔너리
data_dict = {'name' : ['and' , 'bee' , 'cat'] , 'age' : [25 , 30 , 36] , 'city' : ['seoul' , 'busan' , 'incheon']}
y = pd.DataFrame(data_dict)
print(y)

# 데이터프레임 생성3 , pd.DataFrame(넘파이배열 , columns=[열이름])
import numpy as np
data_np = np.array(data_list)
x = pd.DataFrame(data_np , columns=['name' , 'age' , 'city'] , index=['a','b','c'])
print(x)

# 주요 탐색
print(x.shape) # 행/열 크기
print(x.columns) # 컬럼 목록
print(x.index) # 행 목록
print(x.values) # 값만 2차원으로 반환
print(x.head(2)) # 상위n개만 반환
print(x.tail(2)) # 하위n개만 반환
print(x.info()) # 전처리(데이터 정리)하지 전 결측치/타입 확인

# 인덱싱
print(x.iloc[2]) 
print(x.iloc[1,2]) # iloc[행,열]
print(x.loc['a'])
print(x.loc['b','city'])

# 슬라이싱
print(x.iloc[0:2 , 0:1])
print(x.loc['a':'b' , 'name':'age'])

# 새로운 열 추가
x['score'] = [100 , 80 , 95] # 파괴적
print(x)

x = x.assign(score2 = [41 , 52 ,63]) # 비파괴적
print(x)

# 특정한 값 수정
x['age'] = [31,52,51]
print(x)

x.loc['b' , 'age'] = 70 #b행의 age열 값을 70으로 변경
print(x)

x.iloc[0,0] = 'apple'
print(x)

# 여러개 한 번에 수정
#.loc[인덱스 : 끝인덱스 , '컬럼인덱스] = [새로운값]
# x = x.loc[ ['a','b'],'score'] = [10,20]
print(x)

# 필터링 x[조건식] , x[x[열이름]>y]
con1 = x['score2']>70
print(con1)
print(x[con1])

con2 = x['age']>35
print(x[con1&con2])
print(x[con1|con2])

# 필터링 조건으로 새로운 열 추가 또는 수정
x.loc[x['score2']>70 ,'passed'] =True
print(x)

# 열(컬럼) 이름 수정 , .rename(index=() , coloumns=('old':'new))
x = x.rename(columns={'city' : '도시' , 'age' :'나이'})

# 집계 , .describe() : 수치 자료들을 집계 요약
x.describe()
print(x['나이'].sum()) # x[열이름].집계함수()
print(x['score'].mean())
print(x['passed'].value_counts) # 특정열의 빈도 확인



