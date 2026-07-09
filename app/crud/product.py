from sqlalchemy.orm import Session
from app.models.product import Product


def get_products(
    db: Session,
    category: str = None,
    featured: bool = None,
    in_stock: bool = None,
):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if featured is not None:
        query = query.filter(Product.featured == featured)

    if in_stock is not None:
        query = query.filter(Product.in_stock == in_stock)

    return query.all()