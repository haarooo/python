import pandas as pd
# 외부파일 판다스로 불러오기
# 1. .csv 파일 불러오기
df = pd.read_csv(
    './day14/data/data.csv',
    header=0,                # 시작할 행번호(0부터 시작)
    encoding='utf-8'         # 인코딩(한글 : utf-8 , cp949 , euc-kr), 파일마다 다르다
    usecols=['사번' , '이름' , '나이' , '부서'] # 특정한 열만 추출
    na_values=['' , '-' , '미응답' , 'N/A'] # 특정 값을 결측치로 변환
    on_bad_lines='warn'      # 만일 불러오는 중 해당 행 오류 발생 시 제외/패스
    dtype=['사번' : str] # 특정한 열만 타입 수정
    )
print(df)

# 엑셀 파일 (pip install openpyxl) 설치
df = pd.read_excel(
    './day14/data/data.excel',
    sheet_name='Sheet1',         # 특정한 시트만 가져오기
    skiprows=0,
)
print(df)

# json파일 불러오기
df = pd.read_json('./day14/data/data.json')
print(df)

# xml 파일 불러오기 (pip install lmxl)
df = pd.read_xml('./day14/data/data.xml' , xpath='.//row') # xpath='.//가져올태그명' , .현재파일명//(파일 전체에서 찾기) row(마크업명)
print(df)


# 판다스 자료 외부파일 내보내기 
# 1. csv 내보내기
df.to_csv(
    './day14/data/data_out.csv',     # 파일경로
    index=False,                 # 인덱스 제외    
    encoding='utf-8',
    na_rep='Unknown'                    # 결측값 치환 
)

# 2. excel로 내보내기
df.to_excel(
    './day14/data/data_out.xlsx',sheet_name='회원정보'
)

# 3. json으로 내보내기
df.to_json(
    './day14/data/data_out.json',
    orient='records',     # 레코드(리스트) 형식으로 저장
    force_ascii=False     # 한글(유니코드) 유지
    date_format='iso'     # 날짜 형식을 표준 iso 방식 지정  
)

# 4. xml로 내보내기
df.to_xml(
    './day14/data/data_out.xml',
)