from fastapi import Depends, HTTPException, status, Response, APIRouter
from ..database import get_db
from .. import models, schemas, oauth2, utils
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Login"])

@router.post("/login", response_model=schemas.Token)
async def login(credentials : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials!")
    elif not utils.verify_hash(credentials.password, str(user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials!")
    else:
        access_token = oauth2.create_access_token({"user_id" : user.id, "user_email" : user.email})
        return {"access_token" : access_token, "token_type" : "bearer"}
    