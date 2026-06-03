import Enum as Enum
import Optional as Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/figurinha")


class FigurinhaCreateRequest(BaseModel):
    numero: str
    tipo: Enum
    posicao: str


@router.post("/")
async def create_figurinha(request: FigurinhaCreateRequest):
    # mais coisa
    return {"message": "Figurinha criada com sucesso!"}


@router.get("/")
async def get_figurinha(posicao: Optional[str] = None, tipo: Optional[Enum] = None):
    # mais coisa
    if posicao and tipo:
        return {"message": f"Figurinhas do tipo {tipo} e posição {posicao} retornadas!"}
    elif posicao:
        return {"message": f"Figurinhas da posição {posicao} retornadas!"}
    elif tipo:
        return {"message": f"Figurinhas do tipo {tipo} retornadas!"}
    else:
        return {"message": "Todas as figurinhas retornadas!"}


@router.get("/{figurinha_id}")
async def get_figurinha_by_id(figurinha_id: int):
    # mais coisa
    return {"message": f"Figurinha com ID {figurinha_id} retornada!"}


@router.put("/{figurinha_id}")
async def update_figurinha(
    figurinha_id: int, request: FigurinhaCreateRequest
):  # mais coisa
    return {"message": f"Figurinha com ID {figurinha_id} atualizada com sucesso!"}


@router.delete("/{figurinha_id}")
async def delete_figurinha(figurinha_id: int):
    # mais coisa
    return {"message": f"Figurinha com ID {figurinha_id} deletada com sucesso!"}
