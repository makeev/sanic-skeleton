from sanic import Sanic, response
from project.tasks import sleepy_task


app = Sanic.get_app("project")


async def home_view(request) -> response.HTTPResponse:
    return response.json({
        "DB_NAME": app.config.DB_NAME
    })


async def test_view(request, param):
    # async task
    app.add_task(sleepy_task(app, custom_param=param))

    return response.html("<b>test url: <a href='{url}'>home</a></b>".format(
        url=app.url_for('home')
    ))