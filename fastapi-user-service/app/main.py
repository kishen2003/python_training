from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError

from app.api.routes.v1.users import router as user_router
from app.api.routes.v1.health import router as health_router
from app.api.routes.v1.reports import router as reports_router
from app.api.routes.v1.auth import router as auth_router
from app.api.routes.v2.users import router as user_router_v2
from app.core.config import settings
from app.core.logging import logger
from app.exceptions.exceptions import AppException
from app.exceptions.user import (
    UserNotFoundException,
    UserAlreadyExistsException,
)
from app.exceptions.handlers import (
    app_exception_handler,
    user_not_found_handler,
    user_already_exists_handler,
    sqlalchemy_exception_handler,
)

API_V1_PREFIX = "/api/v1"
API_V2_PREFIX = "/api/v2"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("FastAPI application started")
    yield
    # Shutdown
    logger.info("FastAPI application shutting down")

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.ENV == "development",
    lifespan=lifespan,
)

# Register routers
app.include_router(user_router, prefix=API_V1_PREFIX)
app.include_router(health_router, prefix=API_V1_PREFIX)
app.include_router(reports_router, prefix=API_V1_PREFIX)
app.include_router(auth_router, prefix=API_V1_PREFIX)
app.include_router(user_router_v2, prefix=API_V2_PREFIX)
# Register exception handlers
app.add_exception_handler(UserNotFoundException, user_not_found_handler)
app.add_exception_handler(UserAlreadyExistsException, user_already_exists_handler)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)