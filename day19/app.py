
# app.py : FastAPI 실행하는 파일
# controller.py : HTTP REST 파일
# service.py : 로직 파일



# app.py
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 라우터 연결 : 다른 .py에서 정의한 router객체를 합치기
# .include_router(연결할 라우터)
import controller
app.include_router(controller.router)

if __name__ =="__main__":
    uvicorn.run("app:app" , host="127.0.0.1" , port=8000 ,  reload=True)


