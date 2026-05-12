
# FastAPI : 파이썬 웹 프레임워크
# RestAPI : API 문서 자동 생성
# 사용처 : 데이터분석 , AI모델 서버
# 서버 종료 : 터미널 종료 또는 ctrl+c



import uvicorn  # 파이썬 서버 = 자바의 톰캣(WAS) 역할
from fastapi import FastAPI # REST 정의

# app 객체 생성 , 자바와 다르게 파이썬은 인스턴스 생성시 new 없음
app = FastAPI()

# 모듈 실행 시작점
if __name__  == "__main__": # 자바의 main함수 역할
    # spring run 역할
    # uvicorn.run("파일명:app" , host = "현재IP" , port=서버포트 , reload=자동재실행)
    uvicorn.run("T8_01:app" , host="127.0.0.1" , port=8000 , reload=True)
