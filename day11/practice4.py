import numpy as np

# 1. csv 파일 가져오기 ,쉼표로 구분한 자료의 형식
data = np.genfromtxt("./day11/customer_purchase_data.csv" , delimiter=',' , skip_header=1)

# 2. 가져온 데이터의 넘파이 형식 확인
print(data.shape)

# step 1
sales = np.array(data[:,4])
average_purchase = np.mean(sales)
total = np.sum(sales)
print(average_purchase)
print(total)

# step 2 
visit_num = np.array(data[:,1])
vip = data[(visit_num>=20) | (sales>=2000)]
print(vip)
vip_id = vip[:,0]
print(vip_id)



# step 3
arpv = np.array(sales/visit_num)
max_arpv = np.argmax(arpv)
consumer_id = np.array(data[:,0])
print(consumer_id[max_arpv])

# step 4 
cart_item = data[: ,3]
con1 = (visit_num<=3) & (cart_item<=1)
print(np.sum(con1)) # 배열에 전체 True 합계

# step 5 
# 정규화 (값 - 최솟값)/(최댓값 - 최솟값)
# 어떠한 자료들을 0과1사이의 값으로 만들어서(백분율) 비교
data_min = np.min(sales)
data_max = np.max(sales)
nor_data = (sales-data_min)/(data_max-data_min)
vvip = (nor_data>=0.9)
print(vvip)
print(data[vvip])




