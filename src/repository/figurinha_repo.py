from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities import Figurinha 

class FigurinhaRepository(ABC):
    
    @abstractmethod
    def create(self, figurinha: Figurinha) -> Figurinha:
        return

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Figurinha]:
        return

    @abstractmethod
    def find_all(self) -> List[Figurinha]:
        return

    @abstractmethod
    def update_by_id(self) -> Figurinha:
        return
    
    @abstractmethod
    def delete(self, id: int) -> None:
        return