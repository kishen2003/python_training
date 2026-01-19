from fastapi import APIRouter

from app.core.security import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest):
    # Minimal login for demo/reuse; replace with real auth later
    token = create_access_token(subject=data.username)
    return TokenResponse(access_token=token)