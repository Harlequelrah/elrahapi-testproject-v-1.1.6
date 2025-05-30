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
from ..settings.database import database

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..app_three.models import post_tag_table
class Post(database.base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title=Column(String(30),nullable=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship("User",back_populates="posts",lazy="joined")
    tags=relationship("Tag",secondary=post_tag_table,back_populates="posts", lazy="joined")

metadata = database.base.metadata
database.target_metadata = metadata
