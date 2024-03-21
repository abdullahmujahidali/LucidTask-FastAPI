from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models import Post, PostCreate
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/addPost", response_model=Post)
async def add_post(post: PostCreate, current_user: User = Depends(get_current_user)):
    # will be adding Logic to save post and return post ID (Preferably with DB)
    return post

@router.get("/getPosts", response_model=List[Post])
async def get_posts(current_user: User = Depends(get_current_user)):
    # will be adding Logic to return only posts added by the current_user
    return posts