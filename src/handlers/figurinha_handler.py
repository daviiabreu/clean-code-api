from typing import List, Optional

from fastapi import APIRouter, Response
from pydantic import BaseModel

from domain.entities import Figurinha
from service.figurinha_service import FigurinhaService


class FigurinhaCreateRequest(BaseModel):
    numero: Optional[str] = None
    tipo: Optional[str] = None
    posicao: Optional[str] = None


class FigurinhaUpdateRequest(BaseModel):
    numero: Optional[str] = None
    tipo: Optional[str] = None
    posicao: Optional[str] = None


def create_figurinha_router(service: FigurinhaService) -> APIRouter:
    router = APIRouter(prefix="/figurinha", tags=["figurinha"])

    @router.post("", status_code=201)
    def criar(request: FigurinhaCreateRequest) -> Figurinha:
        return service.create_figurinha(request.model_dump())

    @router.get("")
    def listar(
        posicao: Optional[str] = None,
        tipo: Optional[str] = None,
    ) -> List[Figurinha]:
        return service.get_todas_figurinhas(filtro_posicao=posicao, filtro_tipo=tipo)

    @router.get("/{figurinha_id}")
    def obter(figurinha_id: int) -> Figurinha:
        return service.get_figurinha_por_id(figurinha_id)

    @router.put("/{figurinha_id}")
    def atualizar(figurinha_id: int, request: FigurinhaUpdateRequest) -> Figurinha:
        return service.put_figurinha(figurinha_id, request.model_dump())

    @router.delete("/{figurinha_id}", status_code=204)
    def deletar(figurinha_id: int) -> Response:
        service.delete_figurinha(figurinha_id)
        return Response(status_code=204)

    return router
