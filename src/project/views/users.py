from datetime import datetime

from sanic import response
from sanic.views import HTTPMethodView
from sanic_openapi import doc
from webargs import fields, validate

from app import get_app
from helpers import raw_json
from project.models import User
from validation import use_kwargs

app = get_app()


class UsersView(HTTPMethodView):
    async def get(self, request):
        cursor = User.find()
        users = []

        async for doc in cursor:
            users.append(doc.dump())
        return response.json(users)

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
            name=name,
            created_at=datetime.now(),
        )
        await user.commit()

        return response.json(user.dump(), status=201)
