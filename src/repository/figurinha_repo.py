from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities import Figurinha


class FigurinhaRepository(ABC):
    @abstractmethod
    def save(self, figurinha: Figurinha) -> Figurinha: ...

    @abstractmethod
    def find_all(
        self,
        posicao: Optional[str] = None,
        tipo: Optional[str] = None,
    ) -> List[Figurinha]: ...

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Figurinha]: ...

    @abstractmethod
    def update(self, figurinha: Figurinha) -> Optional[Figurinha]: ...

    @abstractmethod
    def delete(self, id: int) -> bool: ...
