from fastapi import APIRouter

import api.cruds.todo as todo_crud
import api.schemas.todo as todo_schema

router = APIRouter()


@router.get("/todos", response_model=list[todo_schema.Todo])
async def list_todos_route():
    return await todo_crud.get_todos()


@router.post("/todo", response_model=todo_schema.TodoCreateResponse)
async def create_todo_route(todo_body: todo_schema.TodoCreate):
    return await todo_crud.create_todo(todo_body)


@router.put("/todo/{todo_id}", response_model=todo_schema.TodoUpdateResponse)
async def update_todo_route(todo_id: int, todo_body: todo_schema.TodoUpdate):
    return await todo_crud.update_todo(todo_id, todo_body)


@router.delete("/todo/{todo_id}", response_model=None)
async def delete_todo_route(todo_id: int):
    return await todo_crud.delete_todo(todo_id)
