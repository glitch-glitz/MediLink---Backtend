from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    slug: str
    category: str
    subcategory: str | None = None
    brand: str | None = None
    sku: str | None = None
    price: float | None = None
    image: str | None = None
    short_description: str | None = None
    description: str | None = None
    in_stock: bool = True
    featured: bool = False


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True