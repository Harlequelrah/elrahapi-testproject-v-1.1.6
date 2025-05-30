from elrahapi.crud.crud_models import CrudModels
from .models import Tag  #remplacer par l'entité SQLAlchemy
from .schemas import TagCreateModel, TagUpdateModel,TagPatchModel,TagReadModel,TagFullReadModel #remplacer par les modèles Pydantic
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import database


myapp_crud_models = CrudModels(
    entity_name="tag",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Tag, #remplacer par l'entité SQLAlchemy
    ReadModel=TagReadModel,
    CreateModel=TagCreateModel, #Optionel
    UpdateModel=TagUpdateModel, #Optionel
    PatchModel=TagPatchModel, #Optionel
    FullReadModel=TagFullReadModel #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=database.session_manager
)
