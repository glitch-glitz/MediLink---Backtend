from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.product import Product
from app.models.order import Order
from app.models.contact import Contact


def get_dashboard_stats(db: Session):
    users = db.query(User).count()

    products = db.query(Product).count()

    orders = db.query(Order).count()

    contacts = db.query(Contact).count()

    pending_orders = (
        db.query(Order)
        .filter(Order.status == "Pending")
        .count()
    )

    revenue = (
        db.query(
            func.sum(Order.total_amount)
        )
        .scalar()
        or 0
    )

    return {
        "users": users,
        "products": products,
        "orders": orders,
        "contacts": contacts,
        "pending_orders": pending_orders,
        "revenue": revenue,
    }