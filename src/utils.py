import aioredis
from sanic import Sanic
from sanic.log import logger


def register_redis(app: Sanic, redis_url, minsize=5, maxsize=10) -> None:
    @app.listener("before_server_start")
    async def init_redis(app, loop):
        app.redis =  await aioredis.create_redis_pool(
            redis_url, minsize=minsize, maxsize=maxsize, loop=loop
        )
        logger.info("Redis pool created")

    @app.listener("after_server_stop")  # type: ignore
    async def close_orm(app, loop):  # pylint: disable=W0612
        if hasattr(app, 'redis'):
            app.redis.close()
            await app.redis.wait_closed()
            logger.info('redis closed')
