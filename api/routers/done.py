from fastapi import APIRouter

import api.cruds.done as done_crud

router = APIRouter()


@router.put("/todo/{todo_id}/done", response_model=None)
async def mark_todo_as_done_router(todo_id: int):
    return await done_crud.mark_todo_as_done(todo_id)


@router.delete("/todo/{todo_id}/done", response_model=None)
async def unmark_todo_as_done_router(todo_id: int):
    return await done_crud.unmark_todo_as_done(todo_id)
