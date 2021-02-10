import settings
from sanic import Sanic
from sanic.log import logger
from tortoise.contrib.sanic import register_tortoise
from sanic_openapi import swagger_blueprint


APP_NAME = "project"
app = Sanic(APP_NAME, strict_slashes=True)
app.blueprint(swagger_blueprint)


def get_app():
    return Sanic.get_app(APP_NAME)


# update sanic config from settings
app.config.update({k: getattr(settings, k) for k in vars(settings) if k.isupper()})

# configure static files
app.static(settings.STATIC_URL, settings.STATIC_PATH)

# ORM and database init
register_tortoise(app, settings.TORTOISE_ORM, generate_schemas=settings.GENERATE_SCHEMAS)

# load middlewares
import middlewares

# load routing
import urls


logger.info('app initialized')