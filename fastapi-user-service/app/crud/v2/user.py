from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.department import Department
from app.schemas.v2.user import UserCreate, UserUpdate
from app.exceptions.user import (
    UserNotFoundException,
    UserAlreadyExistsException,
)

async def create_user(
    db: AsyncSession,
    tenant_id: str,
    user_in: UserCreate,
) -> User:
    # 1. Validate department belongs to tenant
    dept_stmt = select(Department).where(
        Department.id == user_in.department_id,
        Department.tenant_id == tenant_id,
    )
    dept_result = await db.execute(dept_stmt)
    department = dept_result.scalar_one_or_none()

    if not department:
        raise UserNotFoundException(
            "Department does not exist for this tenant"
        )

    # 2. Check email uniqueness within tenant
    user_stmt = select(User).where(
        User.email == user_in.email,
        User.tenant_id == tenant_id,
    )
    user_result = await db.execute(user_stmt)

    if user_result.scalar_one_or_none():
        raise UserAlreadyExistsException(
            f"User with email {user_in.email} already exists"
        )

    # 3. Create user
    user = User(
        name=user_in.name,
        email=user_in.email,
        tenant_id=tenant_id,
        department_id=department.id,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user

async def get_users(
    db: AsyncSession,
    tenant_id: str,
    *,
    skip: int = 0,
    limit: int = 10,
) -> list[User]:
    stmt = (
        select(User)
        .where(User.tenant_id == tenant_id)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_user_by_id(
    db: AsyncSession,
    tenant_id: str,
    user_id: int,
) -> User:
    stmt = select(User).where(
        User.id == user_id,
        User.tenant_id == tenant_id,
    )
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise UserNotFoundException(f"User {user_id} not found")
    return user

async def update_user(
    db: AsyncSession,
    tenant_id: str,
    user_id: int,
    user_in: UserUpdate,
) -> User:
    # 1. Get user scoped to tenant
    user = await get_user_by_id(db, tenant_id, user_id)

    update_data = user_in.model_dump(exclude_unset=True)

    # 2. Handle department change explicitly
    if "department_id" in update_data:
        dept_stmt = select(Department).where(
            Department.id == update_data["department_id"],
            Department.tenant_id == tenant_id,
        )
        dept_result = await db.execute(dept_stmt)
        department = dept_result.scalar_one_or_none()

        if not department:
            raise UserNotFoundException(
                "Department does not exist for this tenant"
            )

        user.department_id = department.id

        # Remove it so it is not set again blindly
        update_data.pop("department_id")

    # 3. Update remaining safe fields
    for field, value in update_data.items():
        setattr(user, field, value)

    await db.commit()
    await db.refresh(user)

    return user

async def delete_user(
    db: AsyncSession,
    tenant_id: str,
    user_id: int,
) -> None:
    user = await get_user_by_id(db, tenant_id, user_id)
    await db.delete(user)
    await db.commit()