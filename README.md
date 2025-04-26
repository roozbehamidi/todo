📝 پروژه Todo App - FastAPI Backend
✨ توضیح کلی پروژه
این پروژه یک اپلیکیشن مدیریت کارها (Todo App) است که با استفاده از تکنولوژی‌های زیر توسعه داده شده:

FastAPI برای توسعه‌ی API

PostgreSQL به عنوان دیتابیس

Docker برای مدیریت محیط توسعه

Railway برای دیپلوی خودکار

GitHub Actions برای CI/CD اتوماتیک

🛠️ تکنولوژی‌ها و ابزارهای استفاده شده
<div align="center"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" alt="Python"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="40" height="40" alt="FastAPI"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="40" height="40" alt="Docker"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="40" height="40" alt="PostgreSQL"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40" height="40" alt="Git"/> </div>
🚀 دموی آنلاین پروژه
🔗 مشاهده‌ی نسخه زنده‌ی Todo App

🏗️ ویژگی‌های اصلی
ثبت نام کاربر (User Registration)

ورود با توکن JWT (Login with JWT)

مدیریت تسک‌های شخصی (Create / Read / Update / Delete Todos)

فیلتر تسک‌ها بر اساس وضعیت تکمیل (Completed / Not Completed)

امنیت API با احراز هویت (OAuth2 Bearer Token)

ساخت خودکار جداول در دیتابیس با SQLAlchemy

پیاده‌سازی CI/CD با GitHub Actions و دیپلوی خودکار روی Railway

کد مرتب با فرمت استاندارد توسط Ruff

🛠️ نحوه اجرا در محیط توسعه
bash
Copy
Edit
# کلون کردن پروژه
git clone https://github.com/roozbehamidi/todo.git

# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای پروژه
uvicorn main:app --reload
📦 داکرایز کردن پروژه
bash
Copy
Edit
# ساخت ایمیج
docker build -t todo-app .

# ران کردن کانتینر
docker run -d -p 8000:8000 todo-app
📊 آمار گیت‌هاب من
![Roozbeh's GitHub stats](https://github-readme-stats.vercel.app/api?username=roozbehamidi&show_icons=true&theme=radical)

✨ تشکر بابت بازدید!
اگر پروژه رو دوست داشتی، ستاره بده! ⭐️