import asyncio

from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.models.department import Department
from app.core.logging import logger

USERS_TO_SEED = [
    {
        "name": "Alice",
        "email": "alice@company.com",
        "department": "HR",
    },
    {
        "name": "Bob",
        "email": "bob@company.com",
        "department": "HR",
    },
    {
        "name": "Carol",
        "email": "carol@company.com",
        "department": "Engineering",
    },
    {
        "name": "Dave",
        "email": "dave@company.com",
        "department": "Engineering",
    },
    {
        "name": "Eve",
        "email": "eve@company.com",
        "department": "Finance",
    },
]

async def seed_users():
    async with AsyncSessionLocal() as session:
        for user_data in USERS_TO_SEED:
            # Check if user already exists
            result = await session.execute(
                select(User).where(User.email == user_data["email"])
            )
            existing_user = result.scalar_one_or_none()
            if existing_user:
                continue
            # Get department
            dept_result = await session.execute(
                select(Department).where(
                    Department.name == user_data["department"]
                )
            )
            department = dept_result.scalar_one_or_none()
            if not department:
                logger.warning(
                    f"Department '{user_data['department']}' not found. Skipping user."
                )
                continue
            user = User(
                name=user_data["name"],
                email=user_data["email"],
                department_id=department.id,
            )
            session.add(user)
        await session.commit()
    logger.info("User seeding completed successfully")

if __name__ == "__main__":
    asyncio.run(seed_users())
