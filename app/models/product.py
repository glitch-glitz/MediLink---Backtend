from sqlalchemy import Boolean, Column, Float, Integer, String, Text

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False, index=True)

    category = Column(String(120), nullable=False)
    subcategory = Column(String(120))

    brand = Column(String(120))
    sku = Column(String(100), unique=True)

    price = Column(Float)

    image = Column(String(500))

    description = Column(Text)
    short_description = Column(Text)

    in_stock = Column(Boolean, default=True)
    featured = Column(Boolean, default=False)