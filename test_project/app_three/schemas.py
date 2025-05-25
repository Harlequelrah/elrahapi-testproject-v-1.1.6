from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

from .meta_models import TagBaseModel

class TagCreateModel(TagBaseModel):
    pass

class TagUpdateModel(TagBaseModel):
    pass

class TagPatchModel(BaseModel):
    libelle: Optional[str] = Field(example="critique",default=None)

class TagReadModel(BaseModel):
    id:int
    libelle:str
    class Config:
        from_attributes=True


class TagFullReadModel(TagReadModel):
    pass
    class Config:
        from_attributes=True
