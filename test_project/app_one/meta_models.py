# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, Field
# from typing import List, Optional

class ProfileBaseModel(BaseModel):
    biography: str = Field(example="i am a tech man")


# class MetaProfileModel(BaseModel):
#     pass
