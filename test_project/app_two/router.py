from typing import List

from elrahapi.router.relationship import Relationship
from elrahapi.router.router_namespace import (
    RELATION_RULES,
    DefaultRoutesName,
    RelationRoutesName,
    TypeRelation,
    TypeRoute,
)
from elrahapi.router.router_provider import CustomRouterProvider

from ..app_three.cruds import myapp_crud as tag_crud
from ..settings.auth.configs import authentication
from ..settings.database import session_manager
from ..settings.auth.cruds import user_crud
from .models import post_tag_table
from .cruds import myapp_crud

user_relation: Relationship = Relationship(
    relationship_name="user",
    second_entity_crud=user_crud,
    second_entity_fk_name="user_id",
    type_relation=TypeRelation.MANY_TO_ONE,
    default_public_relation_routes_name=RELATION_RULES[TypeRelation.MANY_TO_ONE],
)

tag_relation: Relationship = Relationship(
    relation_table=post_tag_table,
    relationship_name="tags",
    second_entity_crud=tag_crud,
    relationship_key1_name="post_id",
    relationship_key2_name="tag_id",
    type_relation=TypeRelation.MANY_TO_MANY_TABLE,
    default_public_relation_routes_name=RELATION_RULES[TypeRelation.MANY_TO_MANY_TABLE],
)
router_provider = CustomRouterProvider(
    prefix="/posts",
    tags=["posts"],
    crud=myapp_crud,
    session_manager=session_manager,
    # authentication=authentication,
    read_with_relations=False,
    relations=[user_relation, tag_relation],
)

app_myapp = router_provider.get_custom_router(routes_name=[DefaultRoutesName.CREATE])
# app_myapp = router_provider.get_protected_router()


