from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.product import (
    get_products,
    get_product,
    get_product_by_slug,
    create_product,
    update_product,
    delete_product,
)
from app.schemas.product import Product, ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/", response_model=List[Product])
def read_products(
    category: str = None,
    featured: bool = None,
    in_stock: bool = None,
    db: Session = Depends(get_db),
):
    return get_products(
        db,
        category=category,
        featured=featured,
        in_stock=in_stock,
    )


@router.get("/{product_id}", response_model=Product)
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = get_product(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("/slug/{slug}", response_model=Product)
def read_product_by_slug(
    slug: str,
    db: Session = Depends(get_db),
):
    product = get_product_by_slug(db, slug)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.post("/", response_model=Product)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return create_product(db, product)


@router.put("/{product_id}", response_model=Product)
def edit_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    updated = update_product(db, product_id, product)

    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated


@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_product(db, product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted successfully"}