from fastapi import APIRouter, Request

import api.cruds.todo as todo_crud
import api.schemas.todo as todo_schema

router = APIRouter()


@router.get("/todos", response_model=list[todo_schema.Todo])
async def list_todos_route(request: Request):
    return await todo_crud.get_todos(request.app)


@router.post("/todo", response_model=todo_schema.TodoCreateResponse)
async def create_todo_route(request: Request,
                            todo_body: todo_schema.TodoCreate):
    return await todo_crud.create_todo(request.app, todo_body)


@router.put("/todo/{todo_id}", response_model=todo_schema.TodoUpdateResponse)
async def update_todo_route(request: Request, todo_id: int,
                            todo_body: todo_schema.TodoUpdate):
    return await todo_crud.update_todo(request.app, todo_id, todo_body)


@router.delete("/todo/{todo_id}", response_model=None)
async def delete_todo_route(request: Request, todo_id: int):
    return await todo_crud.delete_todo(request.app, todo_id)
