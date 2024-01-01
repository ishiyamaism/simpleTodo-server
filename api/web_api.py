from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import done, todo

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


@app.get("/hello")
async def say_hello():
    return "hello!!"

app.include_router(todo.router)
app.include_router(done.router)
