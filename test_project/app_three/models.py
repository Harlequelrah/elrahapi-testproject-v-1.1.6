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

post_tag_table=Table(
    "post_tag",
    database.base.metadata,
    Column('post_id',Integer,ForeignKey('posts.id')),
    Column('tag_id',Integer,ForeignKey('tags.id'))
)

class Tag(database.base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    libelle=Column(String(30),nullable=False)
    posts=relationship("Post",secondary=post_tag_table,back_populates="tags")

metadata= database.base.metadata
database.target_metadata=metadata
