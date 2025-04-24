from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
SessionLocal = None
engine = None

def init_engine():
    from app.core.config import get_database_url
    db_url = get_database_url()
    
    if not db_url:
        raise ValueError("❌ DATABASE_URL is not set!")

    if db_url.startswith("sqlite"):
        eng = create_engine(db_url, connect_args={"check_same_thread": False})
    else:
        eng = create_engine(db_url)

    global engine
    global SessionLocal
    engine = eng
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
