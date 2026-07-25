from fastapi import APIRouter
from app.api.v1.resumes import router as resume_router

api_router=APIRouter()

api_router.include_router(resume_router,prefix="/api/v1/resumes",tags=["Resumes"],)
