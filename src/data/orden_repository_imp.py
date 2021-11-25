from bp import Orden
from bp import Product
from bp import OrdenRepository


class OrdenRepositoryImp:
    def __init__(self) -> None:
        self.orden =[]

    def get_orden_by_id(self, id: str) -> Orden:
        
        print(f"Consulta {id}")
        products = []
        products.append(Product("4", ""))
        products.append(Product("14", ""))
        Orden("123321", "orden 1", "01/01/2021", [])

    def get_product_by_id(self, id: str):
        print(f"Consulta {id}")
        return Product("1", "Jeans")