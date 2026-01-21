import json
import time
from pathlib import Path
from datetime import datetime, timezone

from app.core.logging import logger

BASE_PATH = Path("app/generated/onboarding")
BASE_PATH.mkdir(parents=True, exist_ok=True)


def process_user_onboarding(
    user_id: int,
    email: str,
    tenant_id: str,
):  
    logger.info(f"[ONBOARDING] Started for user={user_id}, tenant={tenant_id}")

    # Prepare onboarding payload
    payload = {
        "user_id": user_id,
        "email": email,
        "tenant_id": tenant_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "steps": [
            "account_created",
            "welcome_message_generated",
            "notification_queued",
        ],
    }

    time.sleep(1)

    # Write onboarding artifact
    file_path = BASE_PATH / f"user_{user_id}.json"
    with open(file_path, "w") as f:
        json.dump(payload, f, indent=4)

    logger.info(f"[ONBOARDING] Artifact created at {file_path}")

    # Simulate external notification
    time.sleep(2)
    logger.info(f"[NOTIFICATION] Welcome email queued for {email}")

    # Simulate downstream system call
    time.sleep(1)
    logger.info(f"[INTEGRATION] User {user_id} sent to analytics service")

    logger.info(f"[ONBOARDING] Completed for user={user_id}")