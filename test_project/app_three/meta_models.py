# Ce fichier sert à créer des metamodels pour ne renvoyer que l'entités  avec une partie ou sans ses relations
from pydantic import BaseModel, Field
from typing import List, Optional

class TagBaseModel(BaseModel):
    libelle:str=Field(example="critique")


class MetaTagModel(BaseModel):
    pass
