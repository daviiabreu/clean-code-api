from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class Figurinha(BaseModel):
    id: int
    numero: int
    tipo: Enum
    posicao: str
    updated_at: Optional[datetime]
    created_at: datetime
