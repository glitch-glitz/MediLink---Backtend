from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.contact import create_contact
from app.schemas.contact import ContactCreate, ContactResponse

router = APIRouter(
    prefix="/contact",
    tags=["Contact"],
)


@router.post("/", response_model=ContactResponse)
def submit_contact(
    contact: ContactCreate,
    db: Session = Depends(get_db),
):
    create_contact(db, contact)

    return ContactResponse(
        success=True,
        message="Your message has been received."
    )