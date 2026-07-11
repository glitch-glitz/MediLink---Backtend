from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.core.dependencies import get_current_user
from app.crud.order import (
    create_order,
    get_my_orders,
)
from app.models.user import User
from app.schemas.order import (
    OrderCreate,
    OrderResponse,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post("/", response_model=OrderResponse)
def checkout(
    order: OrderCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_order(
        db,
        current_user,
        order.items,
    )


@router.get("/my", response_model=List[OrderResponse])
def my_orders(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_my_orders(
        db,
        current_user,
    )