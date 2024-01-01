from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import done, todo
from utils.db import close_db_connection, connect_to_db

app = FastAPI()


# 許可するオリジンのリスト
origins = [
    "http://localhost:3000",
    "https://02.kaizentools.net/api",
]

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのHTTPヘッダーを許可
)


class AppLifespan:
    def __init__(self, app: FastAPI):
        self.app = app

    async def startup(self):
        await connect_to_db(app)

    async def shutdown(self):
        await close_db_connection(app)


lifespan = AppLifespan(app)
app.add_event_handler("startup", lifespan.startup)
app.add_event_handler("shutdown", lifespan.shutdown)


@app.get("/hello")
async def say_hello():
    return "hello!!"

app.include_router(todo.router)
app.include_router(done.router)
