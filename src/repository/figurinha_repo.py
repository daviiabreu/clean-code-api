from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities import Figurinha


class FigurinhaRepository(ABC):
    @abstractmethod
    def create(self, figurinha: Figurinha) -> Figurinha: ...

    @abstractmethod
    def find_all(
        self,
        posicao: Optional[str] = None,
        tipo: Optional[str] = None,
    ) -> List[Figurinha]: ...

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Figurinha]: ...

    @abstractmethod
    def update_by_id(self, id: int, figurinha: Figurinha) -> Optional[Figurinha]: ...

    @abstractmethod
    def delete(self, id: int) -> bool: ...
