from sqlalchemy.orm import Session
from app.models import User, UserCreate, Token, get_db
from app.dependencies import create_access_token
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup", response_model=Token)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    fake_hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
async def login(form_data: UserCreate):
    # need to  replace it with database logic
    authenticated_user_id = "authenticated_user_id"  # validate user credentials
    access_token = create_access_token(data={"sub": form_data.email})
    return {"access_token": access_token, "token_type": "bearer"}
