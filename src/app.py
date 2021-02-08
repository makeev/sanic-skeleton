from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise


app = Sanic("project", strict_slashes=True)
app.config.update({
    "SECRET_KEY": "123"
})
app.static('/static', 'src/static/', name="main_static")

# ORM and database init
register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['project.models']},
    generate_schemas=True
)

# load middlewares
import middlewares

# load routing
import urls
