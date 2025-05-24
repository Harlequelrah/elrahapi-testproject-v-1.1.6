from typing import List

from elrahapi.router.router_namespace import DefaultRoutesName, TypeRoute
from elrahapi.router.router_provider import CustomRouterProvider

from ..settings.auth.configs import authentication
from .cruds import myapp_crud

router_provider = CustomRouterProvider(
    prefix="/posts",
    tags=["posts"],
    crud=myapp_crud,
    # authentication=authentication,
    read_with_relations=False,
)

app_myapp = router_provider.get_custom_router(
    routes_name=[DefaultRoutesName.CREATE]
)
# app_myapp = router_provider.get_protected_router()

# app_myapp = router_provider.get_protected_router()
