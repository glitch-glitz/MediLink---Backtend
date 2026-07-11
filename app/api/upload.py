import os
import shutil

from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

UPLOAD_DIR = "uploads/products"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/image")
def upload_image(
    file: UploadFile = File(...),
):
    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename,
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    return {
        "image_url": f"/uploads/products/{file.filename}"
    }