import time

from app.core.logging import logger

def log_user_creation(user_id: int, email: str):
    logger.info(f"[ONBOARDING] Started for user_id={user_id}")

    # Simulate sending email
    time.sleep(10)
    logger.info(f"[EMAIL] Welcome email sent to {email}")

    # Simulate audit logging
    time.sleep(5)
    logger.info(f"[AUDIT] User {email} created")

    # Simulate default setup
    time.sleep(5)
    logger.info(f"[SETUP] Default preferences created for user_id={user_id}")

    logger.info(f"[ONBOARDING] Completed for user_id={user_id}")