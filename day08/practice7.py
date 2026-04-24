# [ Python Practice7 종합예제]

# 경기도 아파트 실거래가 조회 시스템 ( 리스트와 딕셔너리 사용 )
# 데이터 출처: 국토교통부 실거래가 공개시스템(경기도 최근 1년치 아파트 매매 데이터) 
# https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

# 주요 기능 요구사항
# 1. 데이터 저장 및 로드 (파일 처리)
#     users.txt: 회원 정보 저장 (식별번호,아이디,비밀번호,이름) 직접 생성 
#     아파트(매매)_실거래가_20260424091956.csv: 직접 다운로드한 실거래가 데이터 파일

data_list = []

with open("./day08/apartment.csv" , "r")as file :
    lines = file.readlines()
    header = lines[0].strip().split(",")
    for line in lines[1:]:
        values = line.strip().split(',')
        row_dict = {header[i]: values[i] for i in range(len(header))}
        data_list.append(row_dict)

with open("./day08/apart.txt", 'w' , encoding='utf-8') as file:
    file.write(str(data_list))


# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입, 

users = []

with open("./day08/users.txt" , "w")as f:
    f.write(str(users))

def sign_up(userid, password , name):
    if userid in users:
        print("이미 존재하는 아이디입니다.")
        return False
    

    new_user = {f"아이디":{userid},"비밀번호":{password},"이름":{name}}
    users.append(new_user)
    print("회원가입 성공")
    return True


sign_up("user4", "pass5678", "강호동")  
print(users)

#       - 로그인

def login(username , password):
    global users
    for key,value in users.items():
        if username == key and password == value:
            print("로그인 성공")
        else:
            print("로그인 실패")


login("qqq","eee")

    
#       - 로그아웃
def logout():
    print("로그아웃 성공")


#     2-2) 회원 전용 메뉴: ( 어려운분들은 구현 안해도 됩니다. )
#       - 지역명 검색: '시군구' 열에서 사용자가 입력한 지역명(예: "만안구", "평촌동")이 포함된 모든 거래 내역 출력
#       - 금액 범위 검색: 사용자가 입력한 '최소 금액'과 '최대 금액' 사이의 거래 내역 필터링 출력
#       - 전체 통계 조회: 전체 데이터의 평균 거래가 등 간단한 통계 정보 출력