from datetime import datetime

import aiomysql
from fastapi import FastAPI

import api.schemas.todo as todo_schema


async def create_todo(app: FastAPI,
                      todo_create: todo_schema.TodoCreate) -> todo_schema.Todo:

    async with app.state.db_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            try:

                insert_query = """INSERT INTO todos (title)
                                VALUES (%s)"""
                await cursor.execute(insert_query, (todo_create.title))
                await conn.commit()

                # 最後にINSERTされたIDを取得
                last_id_query = "SELECT LAST_INSERT_ID() as id"
                await cursor.execute(last_id_query)
                result = await cursor.fetchone()
                new_id = result["id"]

            finally:
                await cursor.close()
                conn.close()

            return todo_schema.TodoCreateResponse(
                id=new_id,
                title=todo_create.title,
                done=False  # デフォルト値
            )


async def get_todos(app: FastAPI) -> todo_schema.Todo:
    async with app.state.db_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            try:
                query = "SELECT * FROM todos order by id DESC"
                await cursor.execute(query)
                result = await cursor.fetchall()

            finally:
                await cursor.close()
                conn.close()

            return result


async def update_todo(app: FastAPI,
                      todo_id: int, todo_update: todo_schema.TodoUpdate
                      ) -> todo_schema.TodoUpdateResponse:
    async with app.state.db_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            try:

                # 現在の時刻を取得
                current_time = datetime.now()

                # UPDATEクエリを実行
                query = """UPDATE todos SET
                                title = %s,
                                updated_at = %s
                            WHERE id = %s"""

                await cursor.execute(query,
                                     (todo_update.title,
                                      current_time,
                                      todo_id))
                await conn.commit()

            finally:
                await cursor.close()
                conn.close()

            return todo_schema.TodoUpdateResponse(
                id=todo_id,
                title=todo_update.title,
                done=todo_update.done,
                updated_at=current_time  # 更新した日時を返す
            )


async def delete_todo(app: FastAPI, todo_id: int) -> str:

    async with app.state.db_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            try:
                # DELETEクエリを実行
                query = """DELETE FROM todos
                            WHERE id = %s"""
                await cursor.execute(query, (todo_id,))
                await conn.commit()

                # 削除が成功したかを確認
                if cursor.rowcount > 0:
                    return "Deletion successful"
                else:
                    return "No item was deleted"

            finally:
                await cursor.close()
                conn.close()
