from fastapi import FastAPI

from app.api.products import router as product_router

app = FastAPI(title="MediLink API")


@app.get("/")
def root():
    return {"message": "Welcome to MediLink API"}


app.include_router(product_router)