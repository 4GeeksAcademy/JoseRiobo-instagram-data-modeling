import os
import sys
from sqlalchemy import String, ForeignKey, Column, Integer, Enum
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key = True)
    username = Column(String(250), nullable = False)
    firstname = Column(String(250), nullable = False)
    lastname = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
 
   

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key = True )
    user_from_id = Column(Integer, ForeignKey("person.id"))
    user_to_id = Column(Integer, ForeignKey("person.id"))
    user = relationship(Person)
   
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer,  primary_key=True)
    user_id = Column(Integer, ForeignKey("person.id"))
    person = relationship(Person)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(Enum("type"), nullable= False)
    url = Column(String(250), nullable = False)
    post_id = Column(Integer,ForeignKey("post.id"))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable= False)
    author_id = Column(Integer, ForeignKey("person.id"))
    post_id= Column(Integer, ForeignKey("post.id"))
    person = relationship(Person)
    post = relationship(Post)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
