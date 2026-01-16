from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.core.logging import logger
from app.exceptions.exceptions import AppException
from app.exceptions.user import (
    UserNotFoundException,
    UserAlreadyExistsException,
)


async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    logger.error(
        "Application exception",
        extra={
            "path": request.url.path,
            "error": str(exc),
        },
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException,
):
    logger.warning(
        "User not found",
        extra={
            "path": request.url.path,
            "error": str(exc),
        },
    )
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )


async def user_already_exists_handler(
    request: Request,
    exc: UserAlreadyExistsException,
):
    logger.warning(
        "User already exists",
        extra={
            "path": request.url.path,
            "error": str(exc),
        },
    )
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )


async def sqlalchemy_exception_handler(
    request: Request,
    exc: SQLAlchemyError,
):
    logger.error(
        "Database error",
        extra={
            "path": request.url.path,
            "error": str(exc),
        },
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "Database error"},
    )
