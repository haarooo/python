
# 동적페이지 크롤링
# 웹페이지 자료가 대기 상태가 있는 경우

# 설치 
# pip install playwright # 파이썬 라이브러리
# playwright install # 브라우저 설치

# 라이브러리
import asyncio # 비동기 라이브러리
from playwright.async_api import async_playwright   # 동적 웹페이지 크롤링 라이브러리
import pandas as pd

# 크롤링 주소 : https://search.naver.com/search.naver?where=image&query=짱구
# 박스 : title_item , 이미지 : _fe_image_tab_content_thumbnail_image , 제목 : info_title

# 비동기 웹크롤링

async def naverRun(): # 동기화된 함수
    # 1. playwright 실행하고 p 변수에 결과 대입
    async with async_playwright() as p:
        # 2. await(대기) 상태 이용한 크롬 실행 , await.chromium.launch()
        # headless=False : 브라우저가 직접 실행된다 <봇차단 방자>
        browser = await p.chromium.launch(headless=False)
        
        # 실행된 브라우저(chromium)에서 새로운 페이지에 지정한 URL 대입하여 이동
        url = 'https://search.naver.com/search.naver?where=image&query=짱구'
        page = await browser.new_page() # 새로운 페이지 열기
        await page.goto(url)      # 이동할 url

        # 스크롤 내리이 이벤트(js)
        # (자료가 표시될 때까지 기다리기)대기상태 만들기 , page.wait_for_timeout(초)
        for i in range(2) : # 스크롤 2번 내리기
            await page.wait_for_timeout(3000)
            # window(브라우저).scrollTo(시작위치 , 이동위치)
            # 이동위치 : document(현재 HTML).body(본문).scrollHeight(스크롤 높이) : 즉 현재 브라우저 스크롤을 본문의 가장 하단으로 이동
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        
        # 실행된 페이지에서 특정한 요소 가져오기
        # page.query_selector_all() 여러개 , page.query_selector(식별자) 하나
        items = await page.query_selector_all('.tile_item')
        print(items)

        image_list = [ ]
        for item in items :
            # css선택자 #id , .class , 마크업 , 마크업.class , 
            image_tag = await item.query_selector('img._fe_image_tab_content_thumbnail_image')
            image_link = await image_tag.get_attribute('src') if image_tag else '링크없음' # .get_attribute(속성명) , <마트업 속성명 = 값>

            title_tag = await item.query_selector('.info_title .txt')
            image_title = await title_tag.inner_text() if title_tag else '제목없음'

            image_list.append({'제목' : image_title , '링크' : image_link})

        print(image_list)
            

        # 안전하게 브라우저 닫기 , 
        await browser.close()


asyncio.run(naverRun()) # 동기화된 함수 실행


