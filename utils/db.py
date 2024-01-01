import os

import aiomysql

# 環境ファイルより読み込み
db_config = {
    "user": os.environ.get("USER"),
    "password": os.environ.get("PASSWORD"),
    "database": os.environ.get("DATABASE"),
    "host": os.environ.get("HOST"),
    "port": os.environ.get("PORT"),
    "use_pure": True,
}


async def get_db_connection():
    return await aiomysql.create_pool(
        user=db_config.get("user"),
        password=db_config.get("password"),
        db=db_config.get("database"),
        host=db_config.get("host"),
        port=int(db_config.get("port")) if db_config.get("port") else 3306
    )
