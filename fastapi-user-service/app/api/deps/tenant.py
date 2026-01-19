from fastapi import Header
from typing import Annotated

async def get_tenant_id(
    x_tenant_id: Annotated[str, Header(alias="X-Tenant-ID")],
) -> str:
    """
    Extracts tenant ID from request headers.
    Scoped per request.
    """
    return x_tenant_id