
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# 1. 크롤링 주소 확인 : https://www.yes24.com/product/category/bestseller?categoryNumber=001
# url = "https://www.yes24.com/product/category/bestseller?categoryNumber=001"

# 2. 주소 분석 , 페이지당 개수 , 페이지 번호
# 1~3 페이지 크롤링 예
book_list = []  
for page in range(1 , 4) :
    url = f'https://www.yes24.com/product/category/bestseller?categoryNumber={page}'
    
    # url 요청
    response = requests.get(url)

    # 요청한 url 의 성공했을때 html로 파싱
    soup = BeautifulSoup(response.text , 'html.parser')
    
    # 가져올 식별자 , soup.select() : 여러개선택 , soup.select_one()하나선택
    books = soup.select('#yesBestList > li')

    # 책 여러개 : '#yesBestList > li'
    # 책 하나당 : (.gd_name , yes_b , .info_auth)

    for book in books : 
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        info_auth = book.select_one('.info_auth').get_text().strip().replace('\n' , '')

        # 리스트에 딕셔너리 포함하기
        book_list.append({'제목' : gd_name , '가격' : yes_b , "저자정보" : info_auth})

    # import itme , time.sleep(초) , 지정한 초 만큼 코드(스레드)가 대기상태 , 즉] 서버 과부하 방지
    time.sleep(2)

print(book_list)
df = pd.DataFrame(book_list)
print(df)

