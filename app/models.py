from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from uuid import uuid4, UUID


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Post(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    text: str
    owner_id: UUID


class PostCreate(BaseModel):
    text: str
