
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanfont


df = pd.read_csv(
    './day15/house.csv',
    )
print(df['SalePrice'])

df['SalePrice'].isnull().sum()
df['SalePrice'] = df['SalePrice'].fillna(df['SalePrice'].median())
print(df['SalePrice'])


df['GrLivArea'] = df['GrLivArea'].fillna(df['GrLivArea'].median())

sns.scatterplot( data=df , x='GrLivArea' , y='SalePrice' ,s=30)
plt.title('주거 면적에 따른 가격 분포')
plt.xlabel('주거 면적')
plt.ylabel('판매 가격')
plt.grid()
plt.show()

#지상(지면) 생활 공간 면적(제곱피트) 부동산의 매매 가격(달러). 이것이 바로 예측하려는 목표 변수입니다.
