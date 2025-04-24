from fastapi import FastAPI
from app.routers import auth, todo
import uvicorn
from app.database import init_engine

app = FastAPI(title="TODO API")

@app.on_event("startup")
async def startup_event():
    init_engine()

app.include_router(auth.router)
app.include_router(todo.router)

