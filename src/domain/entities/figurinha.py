from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TipoFigurinha(str, Enum):
    COMUM = "comum"
    BRILHANTE = "brilhante"
    LEGENDS_OURO = "legends_ouro"
    LEGENDS_BRONZE = "legends_bronze"


class Posicao(str, Enum):
    GOLEIRO = "Goleiro"
    ZAGUEIRO = "Zagueiro"
    MEIO_CAMPISTA = "Meio-campista"
    ATACANTE = "Atacante"


class Figurinha(BaseModel):
    id: Optional[int] = None
    numero: str
    tipo: TipoFigurinha
    posicao: Posicao
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
