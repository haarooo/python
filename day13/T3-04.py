
# matplotlib 설치 : pip install matplotlib
# matplotlib import
import matplotlib as mpl
print(mpl.__version__)

# 관례적 import 하는 방법
import matplotlib.pyplot as plt

# 시각화란? 데이터 분석 결과를 시각적으로 표현하여 인사이트(특징) 도출
# 차트내 한글 깨짐 방지 코드(한글폰트)
import matplotlib as mpl
mpl.rc('font', family='Malgun Gothic') # 또는 'Noto Sans CJK JP'
mpl.rcParams['axes.unicode_minus'] = False

# 선 그래프
# 그래프 데이터 준비
x = [0,1,2,3,4,5,6,7,8,9] # x축
y = [9,8,7,6,5,4,3,2,1,0] # y축

# 그래프 설정
plt.plot(x,y)
plt.title('Line Chart') # 차트 제목
plt.xlabel('X-axis') # X축 제목
plt.ylabel('Y축 제목') # y축 제목
plt.grid(True) # 그래프 눈금
# 그래프 출력 
plt.show()

# 선 그래프2
y2 = [0,1,2,3,4,5,6,7,8,9]
plt.plot(x,y, label = '감소하는 선(항목명)' , color='blue' , linestyle = ':')
plt.plot(x,y2, label = '증가하는 선(항목명)' , color='#FF0000' , linestyle = '-')
plt.legend() # 범례에 항목명 표시
plt.show()

# 막대 그래프 .bar(x축 , y축 , width=굵기 , label='항목명' , color='색상')
categories = ['학생1' , '학생2', '학생3' , '학생4']
values = [66,77,88,99]
values2 = [65,75,85,95]
# 막대 겹치지 않게 표시 , width='막대굵기' , x위치
import numpy as np
x = np.arange(len(categories)) # 0부터 x축의 값 개수만큼 생성


plt.bar(x - 0.2 , values , width=0.4 , label='국어성적',color = 'blue')
plt.bar(x+0.2 , values2 ,width=0.4 , label='수학성적' , color='orange')
plt.title('학생 성적 비교')
plt.xlabel('학생명')
plt.ylabel('성적')
plt.legend()
plt.grid(axis='y')
plt.xticks(x , categories) # 위치순으로 라벨 지정
plt.show()

# 파이그래프 , 백분율 , .pie(값 , labels = '항목명' , color='색상' , explode='강조' , startangle=시작각도 , autopct='비율')
labels = ['피자' , '햄버거' , '샐러드' , '파스타']
sizes = [40,30,20,10]
colors = ['gold' , 'lightcoral' , 'lightskyblue' , 'lightgreen']
explode = [0.1 , 0 , 0 , 0] # 원형에서 튀어나오는 정도(강조)
plt.pie(sizes , labels=labels , colors=colors , explode= explode  , startangle=90 , autopct='%1.1f%%') 
# %형식문자 %자릿수,소수자릿수f , f실수 , %%: 형식문자가 아닌 문자 '%'표시
plt.legend()
plt.show()

# 선점도 , 밀집도 , .scatter(x,y , c(color)='색상' , )
x = [1.5 , 2.5 , 3.5 , 4.5 , 5.5]
y = [50 , 60 , 65 , 70 , 75]

plt.scatter(x,y , c='red' , s=100)
plt.grid()
plt.show()

# 히스토그램 , 상관관계 , .hist(값 , color='' , alpha=투명도 , bins=구간개수)

# 샘플 데이터
data=[]
for i in range(50):
    value = sum([ (i*j)%100/100 for j in range(1,13)])
    data.append(value)

# 차트 만들기
plt.hist(data , color='skyblue' , alpha = 0.5 , bins =30)
plt.show()

# 다중 그래프 표현 , .subplot(행 , 열 , figsize=(가로,세로))
fig ,axs = plt.subplots(1, 2 , figsize=(10,7))
# fig : 다중 그래프를 가지고 있는 전체 그 래프 
# axs : 다중 그래프의 위치 , axs[0] 첫번째 그래프
axs[0].plot([1,2,3],[1,4,7])
axs[0].set_title('선그래프')
axs[0].set_xlabel('x축제목')
axs[0].set_ylabel('y축제목')

axs[1].bar([1,2,3],[3,5,2]) 
axs[1].set_title('막대그래프')
axs[1].set_xlabel('x축제목')
axs[1].set_ylabel('y축제목')

# 그래프 이미지(png) 다운로드 , .savefig('파일경로')
plt.savefig('./day13/save_chart.png')


plt.show()

# fig 