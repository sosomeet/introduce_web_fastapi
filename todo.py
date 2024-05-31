# fastapi에서 API Router와 Path를 가져옴
# 라우터는 CRUD를 위해 가져옴
# Path는 경로 파라미터 작성을 위해 가져옴
from fastapi import APIRouter, Path
# model.py 가져옴
from model import Todo

# API Router 객체 생성
todo_router = APIRouter()

todo_list = []

# post == Create
# todo_router를 생성
# id 자동 증가를 위한 변수
count = 0
@todo_router.post("/todo")
# (todo: dict) : todo를 딕셔너리 형태로 받겠다
# (todo: Todo) : todo를 Todo 형태로 받겠다
#  model.py에서 입력 형식을 지정
async def add_todo(todo: Todo) -> dict:
    # id 자동 증가를 위한 코드
    global count
    todo.id = count = count + 1
    todo_list.append(todo)
    return {
        "msg" : "todo added successfully"
    }

# get == Read
# todo_router를 읽음
@todo_router.get("/todo")
async def retrieve_todos()-> dict:
    return {
        "todos" : todo_list
    }

# get == Read
# id로 읽어오는 코드
# 경로 파라미터 설정
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title= "the ID of the todo to retrieve")) -> dict:
    # todo 리스트의 길이만큼 반복
    for todo in todo_list:
        # todo.id가 입력받은 애와 같다면
        if todo.id == todo_id:
            return { "todo" : todo }
    return { "msg": "todo with supplied ID doesn't exist" }


# 삭제 기능
@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title="the ID of the todo to delete")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {
                "msg" : f"Todo with ID {todo_id} deleted successfully"
            }
    return {
            "msg" : "Todo with supplied ID doesn't exist"
    }    