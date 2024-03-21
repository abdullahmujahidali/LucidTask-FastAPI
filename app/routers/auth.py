from fastapi import Depends, HTTPException, APIRouter
from app.models import UserCreate, Token
from app.dependencies import create_access_token, verify_token

router = APIRouter()

@router.post("/signup", response_model=Token)
async def signup(user: UserCreate):
    # need to  replace it with real logic
    user_id = "some_generated_user_id"  # Should be unique
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(form_data: UserCreate):
    # need to  replace it with database logic
    authenticated_user_id = "authenticated_user_id"  # validate user credentials
    access_token = create_access_token(data={"sub": form_data.email})
    return {"access_token": access_token, "token_type": "bearer"}
