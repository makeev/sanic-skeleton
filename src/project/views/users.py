from sanic import response
from sanic.views import HTTPMethodView
from sanic_openapi import doc

from app import get_app
from project.models import User

app = get_app()


class UsersView(HTTPMethodView):
    async def get(self, request):
        users = await User.all()
        return response.json([{"id": u.id, "name": u.name} for u in users])

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

        return response.json({"id": user.id}, status=201)