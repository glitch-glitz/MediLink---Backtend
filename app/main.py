from fastapi import FastAPI

app = FastAPI(title="MediLink API")


@app.get("/")
def root():
    return {
        "message": "Welcome to MediLink API"
    }