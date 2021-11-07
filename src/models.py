import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(100), nullable=True)
    email = Column(String(70), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)
    comment_text = Column(String(1000), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)
    media_type = Column(String(50))
    url = Column(String, nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    follower_user_id = Column(Integer, ForeignKey("user.id"))
    followed_user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')