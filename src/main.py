from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from handlers.figurinha_handler import create_figurinha_router
from infra.database import init_db
from repository.sqlite_figurinha_repo import SQLiteFigurinhaRepository
from service.figurinha_service import (
    FigurinhaService,
    NotFoundError,
    ValidationError,
)


def create_app() -> FastAPI:
    init_db()

    service = FigurinhaService(SQLiteFigurinhaRepository())

    app = FastAPI(title="API de Figurinhas")
    app.include_router(create_figurinha_router(service))

    @app.exception_handler(ValidationError)
    async def handle_validation_error(
        request: Request, exc: ValidationError
    ) -> JSONResponse:
        return JSONResponse(status_code=400, content={"error": str(exc)})

    @app.exception_handler(NotFoundError)
    async def handle_not_found_error(
        request: Request, exc: NotFoundError
    ) -> JSONResponse:
        return JSONResponse(status_code=404, content={"error": str(exc)})

    return app


app = create_app()
