from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from fastapi.exceptions import HTTPException

from typing import Optional
from datetime import datetime, timedelta

from jose import jwt
from jose.exceptions import JWTError

from sqlalchemy.orm import Session
from db.database import get_db
from db.db_user import get_user_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str=Depends(oauth2_scheme), db: Session=Depends(get_db)):
    error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        if not username:
            raise error

    except JWTError:
        raise error

    user = get_user_username(username, db)

    return user
