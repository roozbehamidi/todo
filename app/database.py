from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = None
SessionLocal = None

def init_engine():
    global engine, SessionLocal
    from app.core.config import get_database_url
    db_url = get_database_url()

    print("✅ Connected to DB:", db_url)

    if db_url.startswith("sqlite"):
        engine = create_engine(db_url, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(db_url)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
