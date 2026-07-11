from app.dependencies import get_db, get_current_admin

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
    get_categories,
)
from app.schemas.product import Product, ProductCreate
from app.schemas.category import Category


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/", response_model=List[Product])
def read_products(
    category: str = None,
    featured: bool = None,
    in_stock: bool = None,
    search: str = None,
    sort: str = None,
    skip: int = 0,
    limit: int = 12,
    db: Session = Depends(get_db),
):
    return get_products(
        db=db,
        category=category,
        featured=featured,
        in_stock=in_stock,
        search=search,
        sort=sort,
        skip=skip,
        limit=limit,
    )

@router.get("/categories", response_model=List[Category])
def read_categories(
    db: Session = Depends(get_db),
):
    return get_categories(db)
    
@router.get("/slug/{slug}", response_model=Product)
def read_product_by_slug(
    slug: str,
    db: Session = Depends(get_db),
):
    product = get_product_by_slug(db, slug)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("/{product_id}", response_model=Product)
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = get_product(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.post("/", response_model=Product)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin),
):
    return create_product(db, product)


@router.put("/{product_id}", response_model=Product)
def edit_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin),
):
    updated = update_product(db, product_id, product)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return updated

@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin),
):
    deleted = delete_product(db, product_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return {
        "message": "Product deleted successfully"
    }