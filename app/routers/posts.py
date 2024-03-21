from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from app.models import Post, PostCreate
from app.dependencies import verify_token
from uuid import uuid4

router = APIRouter()

# In-memory "database"
posts_db = {}


@router.post("/addPost", response_model=Post)
async def add_post(post: PostCreate, current_user: str = Depends(verify_token)):
    post_id = str(uuid4())
    new_post = Post(id=post_id, text=post.text, owner_id=current_user.user_id)
    posts_db[post_id] = new_post
    return new_post

@router.get("/getPosts", response_model=List[Post])
async def get_posts(current_user: str = Depends(verify_token)):
    user_posts = [post for post in posts_db.values() if post.owner_id == current_user.user_id]
    return user_posts


@router.delete("/deletePost/{post_id}")
async def delete_post(post_id: UUID, current_user: str = Depends(verify_token)):
    post_id_str = str(post_id)
    if post_id_str in posts_db and posts_db[post_id_str].owner_id == current_user.user_id:
        del posts_db[post_id_str]
        return {"msg": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")
