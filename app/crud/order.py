from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.models.user import User


def create_order(
    db: Session,
    user: User,
    items: list,
):
    total = 0

    order = Order(
        user_id=user.id,
        total_amount=0,
    )

    db.add(order)
    db.flush()

    for item in items:
        product = (
            db.query(Product)
            .filter(Product.id == item.product_id)
            .first()
        )

        if not product:
            continue

        subtotal = product.price * item.quantity
        total += subtotal

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price,
        )

        db.add(order_item)

    order.total_amount = total

    db.commit()
    db.refresh(order)

    return order


def get_my_orders(
    db: Session,
    user: User,
):
    return (
        db.query(Order)
        .filter(Order.user_id == user.id)
        .order_by(Order.id.desc())
        .all()
    )

def get_all_orders(db: Session):
    return (
        db.query(Order)
        .order_by(Order.id.desc())
        .all()
    )


def update_order_status(
    db: Session,
    order_id: int,
    status: str,
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        return None

    order.status = status

    db.commit()
    db.refresh(order)

    return order