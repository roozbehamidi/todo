# create_db.py

from app.database import Base, engine
import app.models  # باعث می‌شه user لود بشه و جدول ثبت بشه

Base.metadata.create_all(bind=engine)

