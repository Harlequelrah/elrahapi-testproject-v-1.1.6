from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

from .meta_models import PostBaseModel

class PostCreateModel(PostBaseModel):
    pass

class PostUpdateModel(PostBaseModel):
    pass

class PostPatchModel(BaseModel):
    title:Optional[str]=Field(example="Le monde d'OZ",default=None)
    user_id:Optional[int]=Field(example=1,default=None)

class PostReadModel(BaseModel):
    id:int
    title:str
    class Config:
        from_attributes=True


class PostFullReadModel(PostReadModel):
    pass
    class Config:
        from_attributes=True
