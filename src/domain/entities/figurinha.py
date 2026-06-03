from typing import Optional

class Product:
    id: int
    name: str
    price: float
    quantity: int


class CreateProductRequest:
    name: str
    price: float
    quantity: int


class UpdateProductRequest:
    price: Optional[float] = None
    quantity: Optional[int] = None
