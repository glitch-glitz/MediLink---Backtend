from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db
from app.crud.contact import create_contact, get_contacts
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
    
def get_contacts(db: Session):
    return (
        db.query(Contact)
        .order_by(Contact.id.desc())
        .all()
    )

@router.get("/", response_model=List[ContactCreate])
def read_contacts(
    db: Session = Depends(get_db),
):
    return get_contacts(db)