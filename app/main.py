from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.products import router as product_router
from app.api.contact import router as contact_router

from app.api.auth import router as auth_router
from app.api.order import router as order_router
from app.api.admin import router as admin_router
from fastapi.staticfiles import StaticFiles
app = FastAPI(title="MediLink API")

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
app.include_router(contact_router)
app.include_router(auth_router)
app.include_router(order_router)
app.include_router(admin_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {"message": "Welcome to MediLink API"}

