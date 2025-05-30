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


class Profile(database.base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    biography=Column(Text,nullable=False)
    user=relationship("User",back_populates="profile",uselist=False)

metadata = database.base.metadata
database.target_metadata = metadata
