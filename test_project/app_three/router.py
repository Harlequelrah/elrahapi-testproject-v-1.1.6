from typing import List

from elrahapi.router.router_namespace import (
    DefaultRoutesName,
    TypeRoute,
    TypeRelation,
    RelationRoutesName,
)
from elrahapi.router.router_provider import CustomRouterProvider
from ..settings.database import session_manager
from ..settings.auth.configs import authentication
from .cruds import myapp_crud

router_provider = CustomRouterProvider(
    prefix="/items",
    tags=["item"],
    crud=myapp_crud,
    session_manager=session_manager,
    # authentication=authentication,
    read_with_relations=False,
)

app_myapp = router_provider.get_public_router()
# app_myapp = router_provider.get_protected_router()

