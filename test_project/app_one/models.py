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


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    biography=Column(Text,nullable=False)
    user=relationship("User",back_populates="profile",uselist=False)

metadata= Base.metadata
