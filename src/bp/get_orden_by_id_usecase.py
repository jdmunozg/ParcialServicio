from bp.orden_repository import OrdenRepository
from dataclasses import dataclass
from bp.domain import Orden

@dataclass
class GetOrdenByIdParams:
    orden_id: str

class GetOrdenByIdUseCase:

    def __init__(self, orden_repository: OrdenRepository) -> None:
        self.orden_repository = orden_repository
    
    def run(self, params: GetOrdenByIdParams) -> Orden:
        orden: Orden = self.orden_repository.get_orden_by_id(params.orden_id)
        products = []
        for product in orden.products:
            products.append(self.orden_repository.get_product_by_id(product.id))
        orden.products = products
        return orden
