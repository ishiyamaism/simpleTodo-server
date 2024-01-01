from datetime import datetime

import aiomysql
from fastapi import FastAPI


async def mark_todo_as_done(app: FastAPI, todo_id: int) -> str:

    async with app.state.db_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            try:

                current_time = datetime.now()

                # UPDATEクエリを実行
                query = """UPDATE todos SET
                                done = 1,
                                updated_at = %s
                            WHERE id = %s"""
                print(query)

                await cursor.execute(query, (current_time, todo_id, ))
                await conn.commit()

                # マークが成功したかを確認
                if cursor.rowcount > 0:
                    return "Mark successful"
                else:
                    return "No item was marked"

            finally:
                await cursor.close()
                conn.close()


async def unmark_todo_as_done(app: FastAPI, todo_id: int) -> str:

    async with app.state.db_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            try:

                current_time = datetime.now()

                # UPDATEクエリを実行
                query = """UPDATE todos SET
                                done = 0,
                                updated_at = %s
                            WHERE id = %s"""
                print(query)

                await cursor.execute(query, (current_time, todo_id, ))
                await conn.commit()

                # アンマークが成功したかを確認
                if cursor.rowcount > 0:
                    return "Unark successful"
                else:
                    return "No item was unmarked"

            finally:
                await cursor.close()
                conn.close()
