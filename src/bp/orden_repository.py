from abc import ABC, abstractmethod
from bp.domain import Orden, Product

class OrdenRepository(ABC):

    @abstractmethod
    def get_orden_by_id(self,id: str) -> Orden:
        pass

    @abstractmethod
    def get_product_by_id(self,id: str) -> Product:
        pass