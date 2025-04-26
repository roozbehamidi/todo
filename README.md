# 📝 Todo App Project – FastAPI Backend

## ✨ Project Summary

The Todo App is a task management application designed with a focus on modern backend development practices. It leverages the following technologies:

- **FastAPI** for high-performance API development
- **PostgreSQL** as a robust relational database
- **Docker** for environment containerization and management
- **Railway** for seamless, automated deployment
- **GitHub Actions** for continuous integration and delivery (CI/CD)

## 🛠️ Technologies and Tools

- Python  
- FastAPI  
- Docker  
- PostgreSQL  
- Git  

## 🚀 Live Demo

🔗 [Access the Live Todo App](#)

## 🏗️ Main Features

- Secure user registration
- Authentication and login via JWT tokens
- Full CRUD operations for personal task management
- Task filtering based on completion status (Completed / Not Completed)
- OAuth2 Bearer Token authentication for API security
- Automated database schema generation with SQLAlchemy
- Full CI/CD workflow with GitHub Actions and automated deployment to Railway
- Codebase formatted and linted according to best practices using Ruff

## 🛠️ Running Locally (Development Setup)

```bash
# Clone the repository
git clone https://github.com/roozbehamidi/todo.git

# Install project dependencies
pip install -r requirements.txt

# Launch the application
uvicorn main:app --reload
```
📦 Docker Setup
```bash
# Build the Docker image
docker build -t todo-app .

# Run the Docker container
docker run -d -p 8000:8000 todo-app
```
📁 Project Structure
```bash
todo/
├── app/
│   ├── auth/             # Authentication and security (JWT, OAuth2)
│   ├── crud/             # CRUD operations for todos and users
│   ├── db/               # Database models and initialization
│   ├── schemas/          # Pydantic models for request and response validation
│   ├── main.py           # Application entry point
│   └── config.py         # Configuration settings
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── .github/workflows/    # GitHub Actions CI/CD workflows
└── README.md             # Project documentation
```
🚀 Future Improvements
Add password reset functionality via email

Implement user roles and permissions

Create an admin dashboard interface

Add rate-limiting and API usage monitoring

Improve test coverage with automated unit and integration tests

Implement WebSocket support for real-time task updates

✨ Thank You!
If you find this project useful or interesting, please consider giving it a ⭐️ on GitHub!
