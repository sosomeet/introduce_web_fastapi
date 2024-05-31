# fast API 받아옴
from fastapi import FastAPI
# CORS 처리를 위해 가져옴
from fastapi.middleware.cors import CORSMiddleware
# todo.py에서 todo_router를 가져옴
from todo import todo_router
# uvicorn 받아옴
import uvicorn

# FastAPI 객체 생성
app = FastAPI()

# CORS를 없애기 위한 내 IP주소와 AWS 주소
origins = ["http://127.0.0.1:5500", "http://18.205.219.133"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @ : decorator
#  app의 동작과 관련해 미리 넣어주는 정보
# .get("/") 밑에 있는 host 주소 뒤에 붙을 주소, /는 루트 경로
#  /dd 하면 0.0.0.0:포트번호/dd 이런 식으로 붙음
@app.get("/")
# async 비동기 방식
# def welcom(): 함수 하나 생성
# -> dict 리턴 형식 명시
async def welcome() -> dict:
    # json format의 return값
    return {
        "msg" : "hello world?"
    }

# API Router를 app에 연결
app.include_router(todo_router)

# main 실행 시
if __name__ == '__main__':
    # uvicorn 사용
    # main = 이 파일 이름
    # app = fastAPI 객체
    # host = 호스트 주소
    #  0.0.0.0은 보통 local host 주소를 의미
    # port = 포트 번호
    # reload = 파이썬 파일 저장 시 웹 사이트 정보 새로고침
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
