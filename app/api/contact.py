from fastapi import APIRouter

from app.schemas.contact import ContactCreate, ContactResponse

router = APIRouter(
    prefix="/contact",
    tags=["Contact"],
)


@router.post("/", response_model=ContactResponse)
def send_contact(contact: ContactCreate):
    print("New contact request")
    print(contact)

    return {
        "message": "Your message has been received."
    }