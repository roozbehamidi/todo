import os

# فقط در حالت لوکال فایل .env رو لود کن
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    from dotenv import load_dotenv
    load_dotenv()

print("🔍 DEBUG: RAILWAY_ENVIRONMENT =", os.getenv("RAILWAY_ENVIRONMENT"))
print("🔍 DEBUG: DATABASE_URL =", os.getenv("DATABASE_URL"))

# این تابع مقدار DATABASE_URL رو فقط زمانی می‌گیره که واقعا نیاز باشه
def get_database_url():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("❌ DATABASE_URL is not set!")
    return db_url

def get_secret_key():
    key = os.getenv("SECRET_KEY")
    if not key:
        raise ValueError("❌ SECRET_KEY is not set!")
    return key

def get_algorithm():
    return os.getenv("ALGORITHM", "HS256")

def get_access_token_expire_minutes():
    return int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


