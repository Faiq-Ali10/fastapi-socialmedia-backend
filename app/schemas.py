from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, conint
from typing import Annotated
from app.models import Base

#User    
class BaseUser(BaseModel):
    email : EmailStr
    phone_number : str
    
class CreateUser(BaseUser):
    password : str
    
class ReturnUser(BaseUser):
    id : int 
    created_at : datetime = Field(alias="timestamp")
    
    model_config = {
        "from_attributes": True
    }
    
#Post

class BasePost(BaseModel):
    title : str
    content : str
    is_published : bool = True

class CreatePost(BasePost):
    pass
    
class ReturnPost(BasePost):
    id : int
    created_at : datetime = Field(alias="timestamp")
    owner_id : int
    owner : ReturnUser
    
    model_config = {
        "from_attributes": True
    }
    
class PostOut(BaseModel):
    Post : ReturnPost
    up_votes : int
    down_votes : int
    
#login
class TokenVerify(BaseModel):
    id : int
    email : EmailStr
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
#Vote
class Vote(BaseModel):
    post_id : int
    direction : Annotated[int, conint(ge=-1, le=1)]
    