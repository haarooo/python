import matplotlib.pyplot as plt
import pandas as pd
import koreanfont
import json

with open('./day14/T5_data.json' , 'r' , encoding='utf-8') as json_file:
    data_json = json.load(json_file)

df_stock = pd.DataFrame(data_json['stock_data'])
print(df_stock.head())

# 기간별 주가와 평균 이동선 선 그래프 표현하고 거래량을 보조축(오른쪽 축) 막대그래프 표현
# plt.subplots() = 한 화면에 여러개 차트 표현 사용
fig , axs = plt.subplots()
axs.plot(df_stock['기간'] , df_stock['주가'] , label='주가' , c='red')
# subplots() 사용 시 라벨 작성 주의할점 : .xlabel -> set_xlabel()
axs.set_xlabel('기간')
axs.set_ylabel('주가')
# 평균 이동선 추가
axs.plot(df_stock['기간'] , df_stock['평균 이동선(3개월)'] , label='평균 이동선(3개월)' , c='blue')
# axs.twinx() , 보조축 = 오른쪽 세로축
axs2 = axs.twinx()
axs2.bar(df_stock['기간']  ,df_stock['거래량'] , label='거래량' , color='gray' , alpha=0.3)
axs2.set_ylabel('거래량')
fig.suptitle('기간별 주가 및 거래량 추세') # 틀 제목
plt.legend()
plt.show()

# 차트 확인 : 1월 부터 12월까지 꾸준히 추세가 우상향

# 주가 , 거래량 , 평균 이동선 가느이 상관관계를 히트맵 표현
import seaborn as sns
# 1. 자료들 간의 상관계수 표현 , ,corr() , 자료들 간의 상관계수(-1 ~ 1)를 자동으로 계산
matrix = df_stock[['주가','거래량','평균 이동선(3개월)']].corr()
print(matrix)
# 상관계수를 히트맵으로 시각화
sns.heatmap(matrix , cmap='coolwarm' , annot=True , fmt='.2f')

#
plt.show()
