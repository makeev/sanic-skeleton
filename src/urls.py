
from app import get_app
from project import views


app = get_app()
app.add_route(views.home_view, "/", name="home")
app.add_route(views.test_view, "/test/<param>/", name="test", methods=["GET"])
app.add_route(views.UsersView.as_view(), "/users/")
