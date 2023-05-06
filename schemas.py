from pydantic import BaseModel
from typing import List


#class article in UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    password: str
    email: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article]

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


#user dakhele article display
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    creator: User

    class Config:
        orm_mode = True
