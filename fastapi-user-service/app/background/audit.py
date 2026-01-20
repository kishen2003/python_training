import time

from app.core.logging import logger

def log_user_creation(user_email: str):
    time.sleep(2)
    logger.info("[AUDIT] User created with email: {user_email}")