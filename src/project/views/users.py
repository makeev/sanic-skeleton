from sanic import Sanic, response
from sanic.views import HTTPMethodView
from project.models import User

app = Sanic.get_app("project")


class UsersView(HTTPMethodView):
    async def get(self, request):
        users = await User.all()
        return response.json([{"id": u.id, "name": u.name} for u in users])