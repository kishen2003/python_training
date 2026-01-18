import asyncio

from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.models.department import Department
from app.core.logging import logger

DEFAULT_DEPARTMENTS = [
    "HR",
    "Engineering",
    "Finance",
    "Operations",
    "Support",
]

async def seed_departments():
    async with AsyncSessionLocal() as session:
        for dept_name in DEFAULT_DEPARTMENTS:
            result = await session.execute(
                select(Department).where(Department.name == dept_name)
            )
            department = result.scalar_one_or_none()
            if not department:
                session.add(Department(name=dept_name))
        await session.commit()
    logger.info("Department seeding completed")

if __name__ == "__main__":
    asyncio.run(seed_departments())
