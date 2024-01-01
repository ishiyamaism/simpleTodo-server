from fastapi import APIRouter, Request

import api.cruds.done as done_crud

router = APIRouter()


@router.put("/todo/{todo_id}/done", response_model=None)
async def mark_todo_as_done_router(request: Request, todo_id: int):
    return await done_crud.mark_todo_as_done(request.app, todo_id)


@router.delete("/todo/{todo_id}/done", response_model=None)
async def unmark_todo_as_done_router(request: Request, todo_id: int):
    return await done_crud.unmark_todo_as_done(request.app, todo_id)
