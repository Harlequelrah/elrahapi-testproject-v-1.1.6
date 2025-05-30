from elrahapi.crud.crud_models import CrudModels
from .models import Profile  #remplacer par l'entité SQLAlchemy
from .schemas import ProfileCreateModel, ProfileUpdateModel,ProfilePatchModel,ProfileReadModel,ProfileFullReadModel #remplacer par les modèles Pydantic
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import database

myapp_crud_models = CrudModels(
    entity_name="profile",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Profile, #remplacer par l'entité SQLAlchemy
    ReadModel=ProfileReadModel,
    CreateModel=ProfileCreateModel, #Optionel
    UpdateModel=ProfileUpdateModel, #Optionel
    PatchModel=ProfilePatchModel, #Optionel
    FullReadModel=ProfileFullReadModel #Optionel
)
myapp_crud = CrudForgery(crud_models=myapp_crud_models, session_manager=database.session_manager)
