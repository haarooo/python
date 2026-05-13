
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import koreanfont

book_list = []

for page in range(1, 10):
    url = f'https://www.yes24.com/product/category/bestseller?pageNumber={page}&pageSize=120&categoryNumber=001'
    response = requests.get(url)
    soup = BeautifulSoup(response.text , 'html.parser')

    books = soup.select('#yesBestList > li')

    # 제목 gd_name  # 가격 yes_b #판매지수 sale_Num # 출파년월 authPub info_date
    for book in books:
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        sale_Num = book.select_one('.saleNum').get_text().strip()
        info_date = book.select_one('.info_date').get_text().strip().replace('\n' , '')

        book_list.append({'제목' : gd_name  , '가격' : yes_b , '판매지수' : sale_Num , '출판년월' : info_date})
    time.sleep(2)

print(book_list)
df = pd.DataFrame(book_list)
print(df)


df.to_csv(
    './project/data/book_data.csv',     # 파일경로
    encoding='utf-8',
    index=False,
    na_rep='Unknown'                    # 결측값 치환 
)


df = pd.read_csv(
    './project/data/book_data.csv',
    header=0,
    encoding='utf-8',
)


# 판매지수 전처리
df['판매지수'] = df['판매지수'].str.replace('판매지수' , '')
print(df['판매지수'])

# 가격 전처리
df['가격'] = df['가격'].str.replace(',' , '')
df['가격'] = df['가격'].astype('int')


# 출판년월 쪼개기
df['출판연도'] = df['출판년월'].str[0:5]
df['출판월'] = df['출판년월'].str[6:]

df = df.drop('출판년월' , axis=1)

df.to_csv(
    './project/data/book_data_final.csv',     # 파일경로
    encoding='utf-8',
    index=False,
    na_rep='Unknown'                    # 결측값 치환 
)



   

