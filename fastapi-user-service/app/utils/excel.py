from io import BytesIO
from datetime import datetime

import pandas as pd

def _to_naive_datetime(value):
    if isinstance(value, datetime) and value.tzinfo is not None:
        return value.replace(tzinfo=None)
    return value

def generate_users_report_excel(rows) -> BytesIO:
    """
    Takes rows returned from get_users_with_department_counts
    and generates an Excel file in memory.
    """
    data = []
    for row in rows:
        data.append(
            {
                "Function": row.function,
                "Count": row.count,
                "User ID": row.id,
                "Name": row.name,
                "Email": row.email,
                "Is Active": row.is_active,
                "Created At": _to_naive_datetime(row.created_at),
                "Updated At": _to_naive_datetime(row.updated_at),
            }
        )
    df = pd.DataFrame(data)
    df = df[
        [
            "Function",
            "Count",
            "User ID",
            "Name",
            "Email",
            "Is Active",
            "Created At",
            "Updated At",
        ]
    ]
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name="Users by Department",
        )
    output.seek(0)
    return output