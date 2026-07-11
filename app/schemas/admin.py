from pydantic import BaseModel


class DashboardStats(BaseModel):
    users: int
    products: int
    orders: int
    contacts: int
    pending_orders: int
    revenue: float