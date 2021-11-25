from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    id: str
    name: str
    def to_json(self):
        return {
            "id":self.id,
            "name": self.name,
            
        }

@dataclass
class Orden:
    id: str
    description: str
    fecha: str
    products : List[Product]

    def to_json(self):
        return {
            "id":self.id,
            "description": self.description,
            "fecha": self.fecha,
            "productos": [prd.to_json() for prd in self.products]
        }