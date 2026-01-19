import asyncio
from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.models.department import Department
from app.core.logging import logger

TENANTS = ["demo_tenant", "acme_corp", "globex"]

DEPARTMENTS = [
    "HR",
    "Engineering",
    "Finance",
    "Operations",
]

async def seed_departments():
    async with AsyncSessionLocal() as session:
        for tenant_id in TENANTS:
            for dept_name in DEPARTMENTS:
                result = await session.execute(
                    select(Department).where(
                        Department.name == dept_name,
                        Department.tenant_id == tenant_id,
                    )
                )
                if not result.scalar_one_or_none():
                    session.add(
                        Department(
                            name=dept_name,
                            tenant_id=tenant_id,
                        )
                    )
        await session.commit()
    logger.info("Departments seeded for tenants: %s", TENANTS)

if __name__ == "__main__":
    asyncio.run(seed_departments())