# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, Field
from typing import List, Optional

class PostBaseModel(BaseModel):
    title:str=Field(example="le monde d'OZ")
    user_id:int=Field(example=1)


class MetaPostModel(BaseModel):
    pass
