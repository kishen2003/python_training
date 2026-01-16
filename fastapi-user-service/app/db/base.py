from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Import all models here so SQLAlchemy can detect them
from app.models.user import User  # noqa