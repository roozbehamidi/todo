from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import DATABASE_URL
#DATABASE_URL = "sqlite:///todo.db"
from app.core.config import get_database_url

DATABASE_URL = get_database_url()

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set!")


if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

