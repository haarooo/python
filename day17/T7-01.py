
# 웹 크롤링 : 웹페이지 존재하는 데이터 수집 하는 기술
# 기초지식 : HTML/CSS
# 파이썬 클로링 라이브러리 : 정적페이지 : request , BeautifulSoup / 동적페이지 : Selenium , Playwright 등
# 클로링(로봇) 허용 여부 확인 : 도메인/robots.txt
#   예) https://www.jobkorea.co.kr/robots.txt , Disallow 불가능 , Allow 가능 
# 적절한 크콜링으로 윤리적 사용

# 1. html/css 식별자 찾기 , #id , .class , 자손선택자 띄어쓰기 , 자식선택자 > )
# 브라우저 개발자도구(F12) -> 왼쪽 상단에 마우스 아이콘 클릭 -> 크롤링 요소 선택 -> 확인

# 파이썬 크롤링
# 1. 주소 : 
#   쿼리스트링 : URL/변수명=값%변수명=값 , 필요한 변수만 정리
#   .url 에서는 한글 불가능
# 2. 크롤링 선택자 : .temperature-text

import requests # URL 요청 라이브러리
from bs4 import BeautifulSoup  # 요청된 URL HTML 조작 라이브러리 

# 1. requests.get(url)
response = requests.get("https://search.daum.net/search?q=안양날씨")
print(response)

# 2. Beautiful(response.text , "html.parser")
soup = BeautifulSoup(response.text , "html.parser")
print(soup) # html 확인

# 3 가져온 HTML에서 특정한 요소(식별자) 가져오기 , soup.select_one(식별자)
txt_temp = soup.select_one('.txt_temp')
print(txt_temp)

# 4. 가져온 요소에서 텍스트만 추출 , <마크업> "텍스트" </마크업> , 
print(txt_temp.get_text())



