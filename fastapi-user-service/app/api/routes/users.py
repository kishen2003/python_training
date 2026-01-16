from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.crud.user import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
)
from app.db.dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_api(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_user(db, user_in)

@router.get(
    "",
    response_model=List[UserResponse],
)
async def get_users_api(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    return await get_users(db, skip=skip, limit=limit)

@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
async def get_user_api(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await get_user_by_id(db, user_id)

@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
async def update_user_api(
    user_id: int,
    user_in: UserUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await update_user(db, user_id, user_in)

@router.patch(
    "/{user_id}",
    response_model=UserResponse,
)
async def patch_user_api(
    user_id: int,
    user_in: UserUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await update_user(db, user_id, user_in)

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user_api(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    await delete_user(db, user_id)