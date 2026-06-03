from abc import ABC, abstractmethod


class FigurinhaRepository(ABC):
    @abstractmethod
    def save(self, figurinha): ...

    @abstractmethod
    def find_all(self, posicao=None, tipo=None): ...

    @abstractmethod
    def find_by_id(self, id): ...

    @abstractmethod
    def update(self, figurinha): ...

    @abstractmethod
    def delete(self, id): ...
