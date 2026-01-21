from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.jobs.deactivate_users import deactivate_inactive_users
from app.core.logging import logger

scheduler = AsyncIOScheduler()

def start_scheduler():
    logger.info("[SCHEDULER] Starting scheduler")

    scheduler.add_job(
        deactivate_inactive_users,
        CronTrigger(hour=0, minute=0),  # Daily at midnight
        id="deactivate_inactive_users",
        replace_existing=True,
    )

    scheduler.start()