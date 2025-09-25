
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.Rol import Rol


class RolRepository(ABC):
    @abstractmethod
    def create(self, rol: Rol) -> None: ...
    @abstractmethod
    def get_all(self) -> List[Rol]: ...
    @abstractmethod
    def get_by_id(self, id_rol: int) -> Optional[Rol]: ...
    @abstractmethod
    def update(self, rol: Rol) -> bool: ...
    @abstractmethod
    def delete(self, id_rol: int) -> bool: ...
