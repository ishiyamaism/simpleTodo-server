import os

import aiomysql
from fastapi import FastAPI

# 環境ファイルより読み込み
db_config = {
    "user": os.environ.get("USER"),
    "password": os.environ.get("PASSWORD"),
    "database": os.environ.get("DATABASE"),
    "host": os.environ.get("HOST"),
    "port": os.environ.get("PORT"),
    "use_pure": True,
}


async def connect_to_db(app: FastAPI):
    app.state.db_pool = await aiomysql.create_pool(
        user=db_config.get("user"),
        password=db_config.get("password"),
        db=db_config.get("database"),
        host=db_config.get("host"),
        port=int(db_config.get("port")) if db_config.get("port") else 3306
    )


async def close_db_connection(app: FastAPI):
    app.state.db_pool.close()
    await app.state.db_pool.wait_closed()
