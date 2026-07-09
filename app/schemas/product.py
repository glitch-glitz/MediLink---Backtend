from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    slug: str
    category: str

    subcategory: Optional[str] = None
    brand: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[float] = None
    image: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None

    in_stock: bool = True
    featured: bool = False


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True