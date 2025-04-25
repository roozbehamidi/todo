from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    from app.database import init_engine
    init_engine()

    from app.routers import auth, todo
    app.include_router(auth.router)
    app.include_router(todo.router)

# ✅ روت اصلی برای تست زنده بودن سرور
@app.get("/")
def root():
    return {
        "message": "✅ API is running! Visit /auth and /todo for available endpoints."
    }


