import matplotlib.pyplot as plt
import pandas as pd
import koreanfont
import json
# json 파일에서 특정한 열만 가져와서 데이터프레임 구성
with open('./day14/T5_data.json' , 'r' , encoding='utf-8') as json_file:
    data_json = json.load(json_file)
df_customer = pd.DataFrame(data_json['customer_data'])
print(df_customer)

# 데이터 분석 /시각화
# 1. 연령대별 총 고객 수 막대그래프
# 여러개 그룹화할 경우에는 .reset_index() 함수 이용해여 행번호 붙인다
newDf = df_customer.groupby(['성별' , '연령대']).agg({'고객 수' : 'sum' , '평균 구매 금액' : 'mean'}).reset_index()
print(newDf)
print(newDf['연령대'])
print(newDf['연령대'].unique())

# 연령대별 고객 수 막대그래프
plt.bar(newDf['연령대'].unique() , newDf.groupby(['연령대']).agg({'고객 수' :'sum'})['고객 수'] , color='blue')
plt.xlabel('연령대')
plt.ylabel('총 고객수')
plt.legend()
plt.title('연령대별 누적 고객 수')
plt.show()

# 2. 성별 = 연령대별 막대 그래프 생성
male_data = newDf[newDf['성별'] =='남성']
female_data = newDf[newDf['성별'] =='여성']
plt.bar(male_data['연령대'] , male_data['고객 수'], label='남성 수' , color='#0000ff')
plt.bar( 
    female_data['연령대'] , 
    female_data['고객 수'] ,
    label ='여성 수' ,
    color = "#ffff00",
    bottom= male_data['고객 수']
)
plt.show()
# 3. 연령대별(그룹) 평균 구매 금액 가로막대 그래프

plt.barh(newDf['연령대'] , newDf['평균 구매 금액'] , color='red')
plt.xlabel('평균 구매 금액')
plt.ylabel('연령대')
plt.title('연령대별 평균 구매 금액')
plt.show()

