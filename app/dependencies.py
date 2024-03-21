from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta

# Secret key for JWT creation/validation - Should be kept secret!
SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"


class TokenData(BaseModel):
    user_id: str


async def get_current_user(token: str = Depends(oauth2_scheme)):
    # will add logic here later
    return user

# Additional dependencies like `oauth2_scheme` definition should go here will be added later
