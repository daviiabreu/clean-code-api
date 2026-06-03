from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class Figurinha(BaseModel):
    id: int
    numero: int
    tipo: Enum
    posicao: str
    updated_at: datetime
    created_at: datetime
