from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, NoneStr
from sqlalchemy import Boolean
from pydantic.types import conint


class UserCreate(BaseModel):
    email:EmailStr
    password:str

class User_Out(BaseModel):
    id:int
    email:EmailStr
    created:datetime
    class Config:
        orm_mode = True

class Userlogin(BaseModel):
    email:EmailStr
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]|None
    
class PostBase(BaseModel):
    title: str
    content: str | None = None
    published: bool = True
    # id:int
    # created:Timestamp  

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    created:datetime
    user_id:int
    user:User_Out
    class Config:
        orm_mode = True

class votepost(BaseModel):
    post_id:int
    dir: conint(le=1) # type: ignore

class PostDetail(BaseModel):
    Posts:Post
    votes:int