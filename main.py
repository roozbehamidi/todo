from fastapi import FastAPI
from app.routers import auth, todo
import uvicorn
from app.database import init_engine

init_engine()
app = FastAPI(title="TODO API")

app.include_router(auth.router)
app.include_router(todo.router)

#if __name__ == "__main__":

#uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
