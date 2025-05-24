from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Table,
)
from ..settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title=Column(String(30),nullable=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship("User",back_populates="posts")

metadata= Base.metadata
