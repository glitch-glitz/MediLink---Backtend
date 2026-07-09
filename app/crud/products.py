from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.product import get_products
from app.schemas.product import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/", response_model=list[Product])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)