from fastapi import APIRouter

from app.utils.async_tasks import run_concurrent_tasks

router = APIRouter(
    prefix="/async-demo",
    tags=["Async Demo"],
)

@router.get("/")
async def async_demo():
    results = await run_concurrent_tasks()
    return {
        "message": "Async tasks executed concurrently",
        "results": results,
    }