from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError

from app.api.routes.users import router as user_router
from app.core.config import settings
from app.core.logging import logger
from app.exceptions.exceptions import AppException
from app.exceptions.handlers import (
    app_exception_handler,
    sqlalchemy_exception_handler,
)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.ENV == "development",
)

# Register routers
app.include_router(user_router)

# Register global exception handlers (infra-level)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)


@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI application started")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("FastAPI application shutting down")
