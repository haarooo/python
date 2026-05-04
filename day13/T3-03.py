import pandas as pd

# 판다스 병합 , .merge( x, y , on='공통컬럼명' , how='inner/outer/left/right')
df_info = pd.DataFrame({'ID': [1,2,3] , 'Name' : ['Ant' , 'Bee' , 'Cat']})
df_score = pd.DataFrame({'ID' : [2,3,4] , 'Score':[88,90,72]})

# 두 판다스 간에 ID가 같은(교집합) 자료 병합
result = pd.merge(df_info , df_score , on='ID' , how='inner')
print(result)


result = pd.merge(df_info , df_score , on='ID' , how='outer')
print(result)


# 판다스 합치기 , .concat([x,y] , axis = 0/1)
result = pd.concat([df_info , df_score] , axis=0 , ignore_index=True)
print(result) # 세로 연결

result = pd.concat([df_info , df_score] , axis=1 , ignore_index=True)
print(result) # 가로 연결

new_score = pd.Series([85,52,35] , name='Score')
df_info['NewScore'] = new_score # 새로운 열에 시리즈 대입
print(df_info)

# 정렬 , .sort_values(by='라벨명')
x = ({'Name':['Ant' , 'Bee' , 'Cat' , 'Dog'] , 'Age':[26 ,22, 21, 24] , 'Score':[66,77,88,99]})
df = pd.DataFrame(x)
df.sort_values(by='Score' , ascending=False)

# 1차정렬 , 2차정렬
result = df.sort_values(by=['Age'  , 'Score'] , ascending=[True , False])
print(result)

# 열이름(라벨) 내림차순으로 정렬
result = df.sort_index(axis=1 , ascending=True)
print(result)

# 그룹
df = pd.DataFrame({
    'Category' : ['A' , "A" , 'B' , 'B' , "A" , 'B'],
    'Type' : ['X' , 'Y' , 'X' , 'Y' , 'X' , 'Y'],
    'Values' : [10,20,30,40,50,60]
})

df.groupby('Category')['Values'].sum()
result = df.groupby('Type')['Values'].mean() # 타입별 값 평균
print(result)

# 다중 그룹
result = df.groupby(['Category' , 'Type'])['Values'].sum()
print(result)

# 다중 집계
result = df.groupby(['Category' , 'Type'])['Values'].agg(['sum' ,'mean' , 'count'])
print(result)
