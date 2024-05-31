# pydantic에서 BaseModel 가져옴
from pydantic import BaseModel

# 각 데이터의 입력 형식 지정
class Todo(BaseModel):
    id: int
    item: str