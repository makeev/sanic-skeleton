from sanic import response

from app import get_app
from project.tasks import sleepy_task


app = get_app()


async def home_view(request) -> response.HTTPResponse:
    return response.json(app.config)


async def test_view(request, param):
    # async task
    app.add_task(sleepy_task(app, custom_param=param))

    return response.html("<b>test url: <a href='{url}'>home</a></b>".format(
        url=app.url_for('home')
    ))