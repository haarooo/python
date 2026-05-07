
import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json


with open('./T5_data.json' , encoding='utf-8') as json_file:
    data_json = json.load(json_file)

df = pd.DataFrame(data_json['financial_performance_data'])

# 플롯박스 : 수익 비용 이익 별 박스 플롯
plt.figure(figsize=(10,6))
plt.boxplot([df['수익'] , df['비용'] , df['이익']] , tick_labels=['수익' , '비용' , '이익'])
plt.title('재무 성과 분포')
plt.ylabel('금액')
plt.show()


# 플롯박스 : 분기별 수익 데이터로 박스플롯 표시
# 플룻박스에서 그룹 , df.boxplot(column['값'] , by='그룹기준')
df.boxplot(column =['수익'] , by='분기')
plt.show()

# 차트확인 : 2분기가 수익 중앙값이 가장 높고 , 1분기가 박스가 길어서 수익이 불안정하다 