from fastapi import FastAPI
from app.routers import auth, todo
import uvicorn

app = FastAPI(title="TODO API")

app.include_router(auth.router)
app.include_router(todo.router)
import os
print("🔍 DATABASE_URL:", os.getenv("DATABASE_URL"))
#if __name__ == "__main__":

#uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
