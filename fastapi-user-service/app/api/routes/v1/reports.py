from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.crud.reports import get_users_with_department_counts
from app.utils.excel import generate_users_report_excel
from app.api.deps import get_current_subject

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)

@router.get("/users-by-department/download")
async def download_users_by_department_report(
    current_subject: str = Depends(get_current_subject),
    db: AsyncSession = Depends(get_db),
):
    """
    Download an Excel report containing:
    - Department (Function)
    - User count per department
    - All user details
    """
    rows = await get_users_with_department_counts(db)
    excel_file = generate_users_report_excel(rows)

    return StreamingResponse(
        excel_file,
        media_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition": (
                "attachment; filename=users_by_department.xlsx"
            )
        },
    )