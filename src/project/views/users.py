from sanic.response import HTTPResponse
from sanic.views import HTTPMethodView
from sanic_openapi import doc
from webargs import fields, validate

from app import get_app
from helpers import raw_json
from project.models import User
from project.serializers import UsersListSerializer, FullUserSerializer
from validation import use_kwargs

app = get_app()


class UsersView(HTTPMethodView):
    async def get(self, request):
        queryset = User.all()
        users = await UsersListSerializer.from_queryset(queryset)
        return raw_json(users.json())

    @doc.consumes(
        doc.String(name="name"),
        location="formData",
        content_type="multipart/form-data"
    )
    @use_kwargs({
        "name": fields.String(
            required=True,
            validate=[validate.Length(min=4), lambda s: s != "Vasya"]
        ),
    }, location='form')
    async def post(self, request, name):
        user = User(
            name=name
        )
        await user.save()

        user = await FullUserSerializer.from_tortoise_orm(user)

        return raw_json(user.json(), status=201)
