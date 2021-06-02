import aioredis

import settings
from sanic import Sanic
from sanic.log import logger
from sanic_openapi import swagger_blueprint

from utils import register_redis, register_tortoise, register_mongo

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
# register_tortoise(app, settings.TORTOISE_ORM, generate_schemas=settings.GENERATE_SCHEMAS)

# register redis
register_redis(
    app, settings.REDIS_URL,
    minsize=settings.REDIS_MIN_POOL_SIZE, maxsize=settings.REDIS_MAX_POOL_SIZE
)

register_mongo(
    app,
    mongo_uri=settings.MONGO_URI,
    mongo_db=settings.MONGO_DB,
    options={
        "minPoolSize": 10,
        "maxPoolSize": 50,
    }
)

# load middlewares
import middlewares

# load routing
import urls

logger.info('app initialized')