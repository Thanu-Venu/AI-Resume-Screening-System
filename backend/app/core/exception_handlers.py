import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import NotFoundException
from app.schemas.error import ErrorDetail,ErrorResponse

logger=logging.getLogger(__name__)

async def not_found_exception_handler(
    request: Request,
    exc: NotFoundException,
)-> JSONResponse:
    logger.warning(
        f"{request.method} {request.url.path} - {exc}"
        )

    error_response=ErrorResponse(
        success=False,
        error=ErrorDetail(
            code="JOB_NOT_FOUND",
            message=str(exc),
        ),
    )
    return JSONResponse(status_code=404,content=error_response.model_dump(),)


def register_exception_handlers(app: FastAPI) -> None:
        app.add_exception_handler(
            NotFoundException,
            not_found_exception_handler,
        )