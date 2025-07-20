from typing import List
from fastapi import Depends, HTTPException, status, Response, APIRouter
from ..database import get_db
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func, case

router = APIRouter(prefix="/post", tags=["Post"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReturnPost)
async def create_post(payload: schemas.CreatePost, db : Session = Depends(get_db), user_data : schemas.TokenVerify = Depends(oauth2.get_current_user)):
    post = models.Post(owner_id = user_data.id,**payload.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/", response_model=List[schemas.PostOut])
async def get_posts(db : Session = Depends(get_db), user_data : schemas.TokenVerify = Depends(oauth2.get_current_user),
                    limit : int = 10, search : str = "", skip : int = 0):
    posts = (
    db.query(
        models.Post,
        func.count(
            case((models.Vote.direction == 1, 1))
        ).label("up_votes"),
        func.count(
            case((models.Vote.direction == -1, 1))
        ).label("down_votes")
    )
    .outerjoin(models.Vote, models.Post.id == models.Vote.post_id)
    .filter(models.Post.title.contains(search))
    .group_by(models.Post.id)
    .limit(limit)   
    .offset(skip)  
    .all()
)
       
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data available")
    else:
        return posts

@router.get("/{id}", response_model=schemas.PostOut)
async def get_post(id : int, db : Session = Depends(get_db), user_data : schemas.TokenVerify = Depends(oauth2.get_current_user)):
    post = (
    db.query(
        models.Post,
        func.count(
            case((models.Vote.direction == 1, 1))
        ).label("up_votes"),
        func.count(
            case((models.Vote.direction == -1, 1))
        ).label("down_votes")
    )
    .outerjoin(models.Vote, models.Post.id == models.Vote.post_id)
    .filter(models.Post.id == id)
    .group_by(models.Post.id)
    .first()
)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data available of id {id}")
    else:
        return post

@router.put("/{id}", response_model=schemas.ReturnPost)
async def update_post(payload: schemas.CreatePost, id : int, db : Session = Depends(get_db), user_data : schemas.TokenVerify = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id, models.Post.owner_id == user_data.id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post Not Found of id {id}")
    
    post = post_query.update({getattr(models.Post, key) : value for key, value in payload.model_dump().items()}, synchronize_session=False)
    db.commit()  
    post = post_query.first()
    return post
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db : Session = Depends(get_db), user_data : schemas.TokenVerify = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id, models.Post.owner_id == user_data.id).first()
    
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post Not Found of id {id}")
    
    db.delete(post)
    db.commit()
    
    return Response(content=f"Post deleted with id {id}")