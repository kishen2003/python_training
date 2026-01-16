from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)
from app.crud.user import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
)
from app.db.dependencies import get_db
from app.exceptions.user import (
    UserNotFoundException,
    UserAlreadyExistsException,
)

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
    try:
        return await create_user(db, user_in)
    except UserAlreadyExistsException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )

@router.get(
    "",
    response_model=List[UserResponse],
    status_code=status.HTTP_200_OK,
)
async def get_users_api(
    db: AsyncSession = Depends(get_db),
):
    return await get_users(db)

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
async def get_user_api(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await get_user_by_id(db, user_id)
    except UserNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
async def update_user_api(
    user_id: int,
    user_in: UserUpdate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await update_user(db, user_id, user_in)
    except UserNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user_api(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    try:
        await delete_user(db, user_id)
    except UserNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )
