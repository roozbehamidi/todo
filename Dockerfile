# --- Base image
FROM python:3.11-slim

# --- Set working directory
WORKDIR /app

# --- Copy project files
COPY . .

# --- Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# --- Set environment variables to be safe
ENV PYTHONUNBUFFERED=1

# --- Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

