from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.exceptions.user import (
    UserNotFoundException,
    UserAlreadyExistsException,
)

async def create_user(
    db: AsyncSession,
    user_in: UserCreate,
    tenant_id: str | None = None,
) -> User:
    stmt = select(User).where(User.email == user_in.email)
    if tenant_id:
        stmt = stmt.where(User.tenant_id == tenant_id)
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise UserAlreadyExistsException(
            f"User with email {user_in.email} already exists"
        )
    user = User(
        name=user_in.name,
        email=user_in.email,
        tenant_id=tenant_id,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_users(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10,
    tenant_id: str | None = None,
) -> list[User]:
    stmt = select(User)
    if tenant_id:
        stmt = stmt.where(User.tenant_id == tenant_id)
    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_user_by_id(
    db: AsyncSession,
    user_id: int,
    tenant_id: str | None = None,
) -> User:
    stmt = select(User).where(User.id == user_id)
    if tenant_id:
        stmt = stmt.where(User.tenant_id == tenant_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise UserNotFoundException(f"User {user_id} not found")
    return user

async def update_user(
    db: AsyncSession,
    user_id: int,
    user_in: UserUpdate,
    tenant_id: str | None = None,
) -> User:
    user = await get_user_by_id(db, user_id, tenant_id)
    for field, value in user_in.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(
    db: AsyncSession,
    user_id: int,
    tenant_id: str | None = None,
) -> None:
    user = await get_user_by_id(db, user_id, tenant_id)
    await db.delete(user)
    await db.commit()