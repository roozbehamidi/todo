import os

if os.getenv("RAILWAY_ENVIRONMENT_NAME") is None:
    from dotenv import load_dotenv
    load_dotenv()

def get_database_url():
    value = os.getenv("DATABASE_URL")
    print("🔍 DEBUG: DATABASE_URL =", value)
    if not value:
        raise ValueError("❌ DATABASE_URL is not set!")
    return value

def get_secret_key():
    value = os.getenv("SECRET_KEY")
    if not value:
        raise ValueError("❌ SECRET_KEY is not set!")
    return value

def get_algorithm():
    return os.getenv("ALGORITHM", "HS256")

def get_access_token_expire_minutes():
    return int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


