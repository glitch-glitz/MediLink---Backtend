from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.products import router as product_router
from app.api.contact import router as contact_router

app = FastAPI(title="MediLink API")

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

@app.get("/")
def root():
    return {"message": "Welcome to MediLink API"}