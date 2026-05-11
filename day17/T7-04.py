
# 동적페이지 크롤링

import asyncio
from playwright.async_api import async_playwright
import pandas as pd

# 크롤링 웹페이지  : https://web.joongna.com/search/코카콜라?page=1

# 동기화 함수
async def joongnaRun() :
    # 브라우저 실행
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 크롤링할 페이지로 이동
        await page.goto('https://web.joongna.com/search/코카콜라?page=1')

        # 해당 페이지가 모두 열렸을때까지 대기 , 시스템상태(인터넷속도) 알 수 없을 때
        # await page.wait_for_load_state('특정상태') , networkidle = 통신 종료 상태
        await page.wait_for_load_state('networkidle')

        # 특정한 검색창 활용
        await page.get_by_placeholder('최소 가격').fill('10,000') # 최소가격
        await page.wait_for_timeout(1000)
        await page.get_by_placeholder('최대 가격').fill('50,000') # 최대가격
        await page.wait_for_timeout(1000)
        
        # 버튼 클릭 이벤트
        apply_button = page.get_by_role('button' , name='적용')
        await apply_button.click()
        await page.wait_for_timeout(3000)

        # 특정한 요소 가져오기
        # 선택자 : a[href^=""]
        items = await page.query_selector_all('div.group > div > a[href^="/product"]')
        # 제품명과 가격 추출
        for item in items : 
            title_tag = await item.query_selector('span.text-14')
            title = await title_tag.inner_text() if title_tag else '없음'

            price_tag = await item.query_selector('span.text-18')
            price = await price_tag.inner_text() if price_tag else '없음'



            item = {'제품명' : title , '가격' : price}
            print(item)


    


asyncio.run(joongnaRun())

