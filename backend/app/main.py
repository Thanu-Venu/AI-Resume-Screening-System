from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging

@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    print("Application is starting up....")

    yield

    print("Application is shutting down....")

app=FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(api_router)

@app.get("/")
def root():
    return{
        "message": f"Welcome to {settings.app_name}!"
    }
