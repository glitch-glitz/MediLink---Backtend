from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


def get_products(
    db: Session,
    category: str = None,
    featured: bool = None,
    in_stock: bool = None,
    search: str = None,
    sort: str = None,
    skip: int = 0,
    limit: int = 12,
):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if featured is not None:
        query = query.filter(Product.featured == featured)

    if in_stock is not None:
        query = query.filter(Product.in_stock == in_stock)

    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    if sort == "price_asc":
        query = query.order_by(Product.price.asc())
    elif sort == "price_desc":
        query = query.order_by(Product.price.desc())
    elif sort == "name":
        query = query.order_by(Product.name.asc())

    return query.offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_product_by_slug(db: Session, slug: str):
    return db.query(Product).filter(Product.slug == slug).first()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        slug=product.slug,
        category=product.category,
        subcategory=product.subcategory,
        brand=product.brand,
        sku=product.sku,
        price=product.price,
        image=product.image,
        short_description=product.short_description,
        description=product.description,
        in_stock=product.in_stock,
        featured=product.featured,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product(db, product_id)

    if not db_product:
        return None

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)

    if not db_product:
        return None

    db.delete(db_product)
    db.commit()

    return db_product