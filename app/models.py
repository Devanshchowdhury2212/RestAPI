from email.policy import default
from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True,nullable=False)
    content = Column(String, nullable = False)
    title = Column(String,nullable = False)
    published = Column(Boolean, server_default = 'True')
    created = Column(TIMESTAMP(timezone=True),nullable = False,server_default = text('now()'))
    user_id = Column(Integer,ForeignKey("users.id",ondelete = "CASCADE"),nullable=False)

    user = relationship("User")

class User(Base):
    __tablename__ = "users" 
    email = Column(String,nullable=False,unique = True)
    password = Column(String,nullable = False)
    id = Column(Integer, primary_key=True,nullable=False)
    created = Column(TIMESTAMP(timezone=True),nullable = False,server_default = text('now()')) 

