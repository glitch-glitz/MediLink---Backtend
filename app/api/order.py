from typing import List

from fastapi import APIRouter, Depends, HTTPException
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

from app.core.dependencies import get_current_admin
from app.schemas.order import OrderStatusUpdate
from app.crud.order import (
    get_all_orders,
    update_order_status,
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

@router.get(
    "/",
    response_model=List[OrderResponse],
)
def all_orders(
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    return get_all_orders(db)


@router.put(
    "/{order_id}",
    response_model=OrderResponse,
)
def change_status(
    order_id: int,
    update: OrderStatusUpdate,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    order = update_order_status(
        db,
        order_id,
        update.status,
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order