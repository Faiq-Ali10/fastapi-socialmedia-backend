from fastapi import Depends, HTTPException, status, APIRouter
from ..database import get_db
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReturnUser)
async def create_User(payload: schemas.CreateUser, db : Session = Depends(get_db)):
    payload.password = utils.get_hash(payload.password)
    user = models.User(**payload.model_dump())
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()  
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email or phone number already exists.")

@router.get("/{id}", response_model=schemas.ReturnUser)
async def get_User(id : int, db : Session = Depends(get_db), user_data : schemas.TokenVerify = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data available of id {id}")
    else:
        return user


