from datetime import datetime

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str | None = Field(None, description="ジョギングをする")
    content: str | None = Field(None, description="野津田町を走る")
    done: bool = Field(False, description="完了フラグ")


class TodoCreate(TodoBase):
    pass


class TodoCreateResponse(TodoCreate):
    id: int


class TodoUpdate(TodoBase):
    pass


class TodoUpdateResponse(TodoUpdate):
    id: int
    updated_at: datetime = Field(
        default_factory=datetime.now, description="更新日時")


class Todo(TodoBase):
    id: int
    created_at: datetime | None
    updated_at: datetime | None
