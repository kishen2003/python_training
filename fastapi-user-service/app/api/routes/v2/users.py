from typing import List

from fastapi import APIRouter, Depends, status, Query, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.v2.user import UserCreate, UserUpdate, UserResponse
from app.crud.v2.user import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
)
from app.db.dependencies import get_db
from app.api.deps.tenant import get_tenant_id
from app.background.audit import log_user_creation

router = APIRouter(
    prefix="/users",
    tags=["Users v2"],
)

@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_api(
    user_in: UserCreate,
    background_tasks: BackgroundTasks,
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
):
    user = await create_user(db=db, user_in=user_in, tenant_id=tenant_id)
    background_tasks.add_task(log_user_creation, user.id, user.email)
    return user

@router.get(
    "",
    response_model=List[UserResponse],
)
async def get_users_api(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
):
    return await get_users(db=db, tenant_id=tenant_id, skip=skip, limit=limit)

@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
async def get_user_api(
    user_id: int,
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
):
    return await get_user_by_id(db=db, user_id=user_id, tenant_id=tenant_id)

@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
async def update_user_api(
    user_id: int,
    user_in: UserUpdate,
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
):
    return await update_user(db=db, user_id=user_id, user_in=user_in, tenant_id=tenant_id)

@router.patch(
    "/{user_id}",
    response_model=UserResponse,
)
async def patch_user_api(
    user_id: int,
    user_in: UserUpdate,
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
):
    return await update_user(db=db, user_id=user_id, user_in=user_in, tenant_id=tenant_id)

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user_api(
    user_id: int,
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
):
    await delete_user(db=db, user_id=user_id, tenant_id=tenant_id)