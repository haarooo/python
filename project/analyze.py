import pandas as pd
import numpy as no
import seaborn as sns
import matplotlib.pyplot as plt

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import koreanfont

df = pd.read_csv(
    './project/data/book_data_final.csv',
    header=0,
    encoding='utf-8',
)
print(df)

# 가격 통계 분석
# 평균 가격
average_price1 = df['가격'].mean()
average_price = int(average_price1)
print(average_price)
# 최고 가격
high_price = df['가격'].max()
print(high_price)
# 최저 가격
low_price = df['가격'].min()
print(low_price)

# 연도별 도서 수 계산
year_count = df['출판연도'].value_counts().sort_index(ascending=False)
print(year_count)
frequent_key = year_count.idxmax()
print(frequent_key)

# 가격 분포 시각화

# 히스토그램 구현
# 가격대별 도서 개수 출력
# 그래프 제목 및 축 이름 출력
plt.figure(figsize=(10,6))
plt.hist(df['가격'] , bins=10 , alpha=0.4 , edgecolor='black')
plt.title('가격대별 도서 개수 분포')
plt.xlabel('가격')
plt.ylabel('도서 수')
plt.show()

# 출판년도별 도서 수 시각화
plt.figure(figsize=(10,6))
year = df['출판연도'].value_counts().index
plt.bar(year , year_count)
plt.title('출판년도별 도서 수')
plt.xlabel('출판년도')
plt.ylabel('도서 수')
plt.show()

stats_dict = [{
    '평균가격' : average_price , 
    '최고가격' : high_price , 
    '최저가격' : low_price,
    '최다출판연도' : frequent_key
    }]

stats_df = pd.DataFrame(stats_dict)





