from elrahapi.authentication.authentication_router_provider import AuthenticationRouterProvider

from elrahapi.authentication.authentication_manager import AuthenticationManager
from ..secret import (
    USER_MAX_ATTEMPT_LOGIN,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRATION,
    REFRESH_TOKEN_EXPIRATION,
)
from .cruds import user_crud_models
from ..database import session_manager
from elrahapi.router.route_additional_config import AuthorizationConfig
from elrahapi.router.router_routes_name import DefaultRoutesName
authentication = AuthenticationManager(
    secret_key=SECRET_KEY,
    algorithm=ALGORITHM,
    access_token_expiration=ACCESS_TOKEN_EXPIRATION,
    refresh_token_expiration=REFRESH_TOKEN_EXPIRATION,
    session_manager=session_manager,
)


user_crud_models.sqlalchemy_model.MAX_ATTEMPT_LOGIN = USER_MAX_ATTEMPT_LOGIN
authentication.authentication_models=user_crud_models
authentication_router_provider = AuthenticationRouterProvider(
    authentication=authentication,
    session_manager=session_manager,
    )
authentication_router = authentication_router_provider.get_auth_router()
