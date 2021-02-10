from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from project.models import User

UserSerializer = pydantic_model_creator(User, exclude=('id',), name="short_user")
UsersListSerializer = pydantic_queryset_creator(User, name="short_user")

# @BUG https://github.com/tortoise/tortoise-orm/pull/639
FullUserSerializer = pydantic_model_creator(User, name="all_user_fields")
FullUsersListSerializer = pydantic_queryset_creator(User, name="all_user_fields")


