# app/celery_worker.py

from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("worker", broker=REDIS_URL)

@celery_app.task
def example_task(name):
    print(f"✅ Task executed! Hello, {name}")
