from sanic import response
from sanic.views import HTTPMethodView

from app import get_app
from project.models import User

app = get_app()


class UsersView(HTTPMethodView):
    async def get(self, request):
        users = await User.all()
        return response.json([{"id": u.id, "name": u.name} for u in users])