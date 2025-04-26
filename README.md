# 📝 Todo App with FastAPI

یک پروژه‌ی مدیریت کارها (Todo App) ساخته شده با FastAPI و PostgreSQL.

## 🚀 ویژگی‌ها
- ثبت‌نام و ورود کاربران (Authentication with JWT)
- ساخت، مشاهده، ویرایش و حذف وظایف (Todos)
- حفاظت مسیرها با OAuth2 Bearer Token
- داکیومنت خودکار API با Swagger UI

## 📦 تکنولوژی‌ها
- FastAPI
- PostgreSQL
- SQLAlchemy
- Railway (Hosting)
- GitHub Actions (CI/CD)

## 📄 پیش‌نیازها
- Python 3.11+
- Git
- Railway account

## ⚙️ نصب و اجرا در لوکال
```bash
git clone https://github.com/roozbehamidi/todo.git
cd todo
pip install -r requirements.txt
uvicorn main:app --reload
