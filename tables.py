'''ORM database table classes'''
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    '''Base ORM class'''


class User(Base):
    '''User class'''
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement="auto")
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    posts: Mapped[List["Post"]] = relationship(back_populates="user")


class Post(Base):
    '''Post class'''
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement="auto")
    title = Column(String)
    content = Column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="posts")
