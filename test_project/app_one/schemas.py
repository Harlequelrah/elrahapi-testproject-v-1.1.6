from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

from .meta_models import ProfileBaseModel

class ProfileCreateModel(ProfileBaseModel):
    pass

class ProfileUpdateModel(ProfileBaseModel):
    pass

class ProfilePatchModel(BaseModel):
    biography: Optional[str] = Field(example="i am a tech man",default=None)

class ProfileReadModel(BaseModel):
    id:int
    biography:str
    class Config:
        from_attributes=True


class ProfileFullReadModel(ProfileReadModel):
    pass
    class Config:
        from_attributes=True
