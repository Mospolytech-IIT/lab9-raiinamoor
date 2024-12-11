'''Pydantic schemas'''
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    '''Pydantic schema for the User table'''
    id: int
    username: str
    email: str
    password: str


class PostBaseSchema(BaseModel):
    '''Pydantic schema for the Post table'''
    id: int
    title: str
    content: str
    user_id: int
