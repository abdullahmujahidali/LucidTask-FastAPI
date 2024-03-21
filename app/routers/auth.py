from fastapi import APIRouter, HTTPException, Depends, status
from app.models import UserCreate, Token
from app.dependencies import create_access_token

router = APIRouter()

@router.post("/signup", response_model=Token)
async def signup(user: UserCreate):
    # logic to hash password, save user and generate token
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
async def login(form_data: UserCreate):
    #  logic to authenticate user and generate token
    return {"access_token": token, "token_type": "bearer"}