import asyncio
from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.models.department import Department
from app.core.logging import logger

TENANT_USERS = {
    "demo_tenant": [
        {"name": "Alice", "email": "alice@company.com", "department": "HR"},
        {"name": "Mark", "email": "mark@company.com", "department": "HR"},
        {"name": "Bob", "email": "bob@company.com", "department": "Engineering"},
        {"name": "Carol", "email": "carol@company.com", "department": "Engineering"},
        {"name": "Dave", "email": "dave@company.com", "department": "Engineering"},
        {"name": "Eve", "email": "eve@company.com", "department": "Finance"},
        {"name": "Frank", "email": "frank@company.com", "department": "Operations"},
    ],
    "acme_corp": [
        {"name": "Alice", "email": "alice@acme.com", "department": "HR"},
        {"name": "Charlie", "email": "charlie@acme.com", "department": "Finance"},
        {"name": "Irene", "email": "irene@acme.com", "department": "Finance"},
        {"name": "Bob", "email": "bob@acme.com", "department": "Engineering"},
        {"name": "Henry", "email": "henry@acme.com", "department": "Engineering"},
        {"name": "Laura", "email": "laura@acme.com", "department": "Operations"},
    ],
    "globex": [
        {"name": "Dave", "email": "dave@globex.com", "department": "Engineering"},
        {"name": "Ivy", "email": "ivy@globex.com", "department": "Engineering"},
        {"name": "Bob", "email": "bob@globex.com", "department": "HR"},
        {"name": "Nina", "email": "nina@globex.com", "department": "HR"},
        {"name": "Oscar", "email": "oscar@globex.com", "department": "Finance"},
        {"name": "Paul", "email": "paul@globex.com", "department": "Operations"},
        {"name": "Quinn", "email": "quinn@globex.com", "department": "Operations"},
    ],
}

async def seed_users():
    async with AsyncSessionLocal() as session:
        for tenant_id, users in TENANT_USERS.items():
            for user_data in users:
                # Check if user already exists for this tenant
                result = await session.execute(
                    select(User).where(
                        User.email == user_data["email"],
                        User.tenant_id == tenant_id,
                    )
                )
                if result.scalar_one_or_none():
                    continue
                # Get department for same tenant
                dept_result = await session.execute(
                    select(Department).where(
                        Department.name == user_data["department"],
                        Department.tenant_id == tenant_id,
                    )
                )
                department = dept_result.scalar_one_or_none()
                if not department:
                    logger.warning(
                        "Department '%s' not found for tenant '%s'",
                        user_data["department"],
                        tenant_id,
                    )
                    continue
                session.add(
                    User(
                        name=user_data["name"],
                        email=user_data["email"],
                        tenant_id=tenant_id,
                        department_id=department.id,
                    )
                )
        await session.commit()
    logger.info("Users seeded for all tenants")

if __name__ == "__main__":
    asyncio.run(seed_users())
