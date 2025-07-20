from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/vote", tags=["Vote"])

@router.post("/")
async def vote(payload: schemas.Vote, db : Session = Depends(get_db), user_data : schemas.TokenVerify = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == payload.post_id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {payload.post_id} does not exist")
    
    if payload.direction == 1:
        vote_found = db.query(models.Vote).filter(models.Vote.post_id == payload.post_id, models.Vote.user_id == user_data.id, models.Vote.direction == payload.direction).first()
        if vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="you already up voted!")
        else:
            delete_vote = db.query(models.Vote).filter(models.Vote.post_id == payload.post_id, models.Vote.user_id == user_data.id).first()
            if delete_vote:
                db.delete(delete_vote)
                db.commit()
            
            vote = models.Vote(**payload.model_dump(), user_id = user_data.id)
            db.add(vote)
            db.commit()
            db.refresh(vote)
            return Response(status_code=status.HTTP_201_CREATED, content="post up voted successfully!")
    elif payload.direction == 0:
        vote_found = db.query(models.Vote).filter(models.Vote.post_id == payload.post_id, models.Vote.user_id == user_data.id).first()
        if not vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="you don't voted already!")
        else:
            delete_vote = db.query(models.Vote).filter(models.Vote.post_id == payload.post_id, models.Vote.user_id == user_data.id).first()
            if delete_vote:
                db.delete(delete_vote)
                db.commit()
            return Response(status_code=status.HTTP_201_CREATED, content="voted removed successfully")      
    else:
        vote_found = db.query(models.Vote).filter(models.Vote.post_id == payload.post_id, models.Vote.user_id == user_data.id, models.Vote.direction == payload.direction).first()
        if vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="you already up down voted!")
        else:
            delete_vote = db.query(models.Vote).filter(models.Vote.post_id == payload.post_id, models.Vote.user_id == user_data.id).first()
            if delete_vote:
                db.delete(delete_vote)
                db.commit()
            
            vote = models.Vote(**payload.model_dump(), user_id = user_data.id)
            db.add(vote)
            db.commit()
            db.refresh(vote)
            return Response(status_code=status.HTTP_201_CREATED, content="post down voted successfully!")            
        
        
                
            
    
    
    