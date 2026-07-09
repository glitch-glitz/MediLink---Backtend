from sqlalchemy.orm import Session

from app.models.contact import Contact
from app.schemas.contact import ContactCreate


def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(
        name=contact.name,
        email=contact.email,
        subject=contact.subject,
        message=contact.message,
    )

    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    return db_contact


def get_contacts(db: Session):
    return (
        db.query(Contact)
        .order_by(Contact.id.desc())
        .all()
    )