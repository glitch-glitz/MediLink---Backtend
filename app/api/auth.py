from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.user import (
    create_user,
    authenticate_user,
    get_user_by_email,
)
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    Token,
)
from app.core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db),
):
    existing = get_user_by_email(db, user.email)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    create_user(
        db,
        user.name,
        user.email,
        user.password,
    )

    return {
        "message": "User created successfully"
    }


@router.post("/login", response_model=Token)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db,
        credentials.email,
        credentials.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    token = create_access_token(
        {
            "sub": user.email,
            "admin": user.is_admin,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }