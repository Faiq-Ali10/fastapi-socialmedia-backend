from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, status, HTTPException
from pytest import Session
from fastapi.security import OAuth2PasswordBearer
from . import database, models, schemas
from sqlalchemy.orm import Session
from .config import settings

from app.database import get_db

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict) -> str:
    data["exp"] = int((datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp())
    return jwt.encode(data, SECRET_KEY, ALGORITHM)

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id = payload.get("user_id")
        email = payload.get("user_email")
        if id is None or email is None:
            raise credentials_exception
        
        token_data = schemas.TokenVerify(id=id, email=email)
    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token : str = Depends(oauth_scheme), db : Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token_data = verify_token(token, credentials_exception)

    return db.query(models.User).filter(models.User.id == token_data.id).first()


