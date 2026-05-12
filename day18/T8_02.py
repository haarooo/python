
import uvicorn
from fastapi import FastAPI

# FastAPI 객체 생성
app = FastAPI()

# 서버 실행
if __name__ == "__main__" :
    uvicorn.run("T8_02:app" , host='127.0.0.1' , port=8000 , reload=True)


# Rest 정의하기
# REST : 자원 주고 받는 상태 구조
# REST API : HTTP로 REST 구현한 아키텍처
# 자동으로 JSON 타입으로 응답한다

@app.get("/") # HTTP GET 방식으로 매핑한다 # 주소 정의
async def index() :
    return "안녕"

# 쿼리 파라미터
@app.get('/user')
async def find_user(name , age:int): # URL?변수=값&변수명=값 , 기본타입 str # 변수명 : 타입
    return {'name' : name , 'age' : age , 'msg' : '쿼리스트링예시'}

# 경로 파라미터
@app.get('/item/{name}/{age}')
async def find_item(name : str , age : int):
    return {'name' : name , 'age' : age , 'msg' : '경로파라미터예시'}

# 본문(body)            # POST/PUT
@app.post("/product")
async def find_product(product : dict) : # 변수명 : dict , 딕셔너리 타입
    return product

# RESTAPI 테스트 : 1. TalendAPI , 2. PostMan , 3. FastAPi docs



