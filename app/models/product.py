from sqlalchemy import Boolean, Column, Float, Integer, String, Text

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True)

    category = Column(String(100), nullable=False)
    subcategory = Column(String(100))

    brand = Column(String(100))
    sku = Column(String(100), unique=True)

    price = Column(Float)

    image = Column(String(500))

    short_description = Column(Text)
    description = Column(Text)

    in_stock = Column(Boolean, default=True)
    featured = Column(Boolean, default=False)