from pydantic.schema import ROOT_KEY
from sanic import response
from sanic.views import HTTPMethodView
from sanic_openapi import doc

from app import get_app
from project.models import User
from project.serializers import UsersListSerializer, FullUserSerializer

app = get_app()


class UsersView(HTTPMethodView):
    async def get(self, request):
        queryset = User.all()
        users = await UsersListSerializer.from_queryset(queryset)
        return response.json(users.dict()[ROOT_KEY])

    @doc.consumes(
        doc.String(name="name"),
        location="formData",
        content_type="multipart/form-data"
    )
    async def post(self, request):
        user = User(
            name=request.form.get("name")
        )
        await user.save()

        user = await FullUserSerializer.from_tortoise_orm(user)

        return response.json(user.dict(), status=201)
