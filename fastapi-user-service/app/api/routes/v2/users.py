from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users v2"],
)

@router.get("/")
async def get_users_v2():
    return {
        "message": "This is v2 of the users API",
        "note": "Response shape can evolve without breaking v1",
    }