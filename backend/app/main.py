from fastapi import FastAPI
from app.api.router import api_router
app=FastAPI(title="AI Resume Screening System",description="An AI-powered resume screening system that helps recruiters to screen resumes quickly and efficiently.",version="1.0.0",)

app.include_router(api_router)

@app.get("/")
def root():
    return{
        "message":"Welcome to the AI resume screening system!"
    }
