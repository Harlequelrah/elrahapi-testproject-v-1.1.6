from elrahapi.crud.crud_models import CrudModels
from .models import Post  #remplacer par l'entité SQLAlchemy
from .schemas import PostCreateModel, PostUpdateModel,PostPatchModel,PostReadModel,PostFullReadModel #remplacer par les modèles Pydantic
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import database


myapp_crud_models = CrudModels(
    entity_name="post",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Post, #remplacer par l'entité SQLAlchemy
    ReadModel=PostReadModel,
    CreateModel=PostCreateModel, #Optionel
    UpdateModel=PostUpdateModel, #Optionel
    PatchModel=PostPatchModel, #Optionel
    FullReadModel=PostFullReadModel #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=database.session_manager
)
