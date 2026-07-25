from fastapi import APIRouter

router=APIRouter()

@router.get("/")
def get_resumes():
    return{
        "message":"List of resumes"
    }