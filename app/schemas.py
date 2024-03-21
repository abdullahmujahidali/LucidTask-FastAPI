from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID, uuid4


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[str] = None


class PostBase(BaseModel):
    text: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: UUID = uuid4()
    owner_id: str

    class Config:
        orm_mode = True
