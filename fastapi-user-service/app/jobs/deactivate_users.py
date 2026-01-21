from datetime import datetime, timedelta, timezone

from sqlalchemy import update
from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.core.config import settings
from app.core.logging import logger


async def deactivate_inactive_users():
    """
    Cron job:
    Deactivate users inactive for N days
    """
    logger.info("[CRON] Deactivate inactive users job started")

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=settings.USER_INACTIVITY_DAYS)

    async with AsyncSessionLocal() as session:
        stmt = (
            update(User)
            .where(
                User.is_active.is_(True),
                User.updated_at < cutoff_date,
            )
            .values(is_active=False)
        )

        result = await session.execute(stmt)
        await session.commit()

        logger.info(f"[CRON] Deactivated {result.rowcount} inactive users")