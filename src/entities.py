from pydantic import BaseModel
from enum import Enum
from typing import Optional

class ProductCategory(Enum):
    may_khoan = "may khoan"

class ProductInfo(BaseModel):
    """
    A class represents product info from the web returned by a web scrapper.
    """
    url: str
    title: str
    mall: bool
    category: ProductCategory
    model: Optional[str] = None
    images: list[str]
    basePrice: tuple[int, int]
    price: tuple[int, int]
    properties: dict[str, str]
    description: str

class ModelInfo(BaseModel):
    """
    A class represents the model of a product category which a validator can use to check product info against.
    """
    name: str
    category: ProductCategory
    price: tuple[int, int]

class ValidateResult(BaseModel):
    image_includes_brand: bool
    text_includes_brand: bool
    known_model: Optional[str]
    old_product: bool
    low_price: bool
    is_fake: bool
