from fastapi import APIRouter
from app.core.exceptions import JobNotFoundException

router = APIRouter()

@router.get("/")
async def get_jobs():
    return {"message": "Get Jobs"}
    
@router.get("/test-exception")
async def test_exception():
    raise JobNotFoundException(42)