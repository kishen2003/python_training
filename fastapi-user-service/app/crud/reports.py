from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.department import Department

async def get_users_with_department_counts(
    session: AsyncSession,
):
    """
    Returns user-level rows enriched with:
    - department name
    - user count per department
    """
    # Subquery: count users per department
    department_count_subquery = (
        select(
            User.department_id.label("department_id"),
            func.count(User.id).label("user_count"),
        )
        .group_by(User.department_id)
        .subquery()
    )
    # Main query: users + department + count
    query = (
        select(
            Department.name.label("function"),
            department_count_subquery.c.user_count.label("count"),
            User.id,
            User.name,
            User.email,
            User.is_active,
            User.created_at,
            User.updated_at,
        )
        .join(User, User.department_id == Department.id)
        .join(
            department_count_subquery,
            department_count_subquery.c.department_id == Department.id,
        )
        .order_by(Department.name, User.id)
    )
    result = await session.execute(query)
    return result.all()
