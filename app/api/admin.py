from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.core.dependencies import get_current_admin
from app.crud.admin import get_dashboard_stats
from app.schemas.admin import DashboardStats

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get(
    "/dashboard",
    response_model=DashboardStats,
)
def dashboard(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    return get_dashboard_stats(db)