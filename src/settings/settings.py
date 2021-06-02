import os

USE_TZ = False
TIMEZONE = 'UTC'
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

PG_MIN_POOL_SIZE = int(os.getenv('PG_MIN_POOL_SIZE', 1))
PG_MAX_POOL_SIZE = int(os.getenv('PG_MIN_POOL_SIZE', 10))

REDIS_MIN_POOL_SIZE = int(os.getenv('REDIS_MIN_POOL_SIZE', 1))
REDIS_MAX_POOL_SIZE = int(os.getenv('REDIS_MAX_POOL_SIZE', 10))

AUTH_TOKEN = None

# DB
TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.asyncpg',
            "credentials": {
                "user": DB_USER,
                "password": DB_PASSWORD,
                "host": DB_HOST,
                "port": DB_PORT,
                "database": DB_NAME
            },
            "minsize": PG_MIN_POOL_SIZE,
            "maxsize": PG_MAX_POOL_SIZE
        }
    },
    "apps": {
        "models": {
            "models": [
                "project.models",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
    'use_tz': USE_TZ,
    'timezone': TIMEZONE
}

REDIS_URL = 'redis://localhost'

# create empty database on init
GENERATE_SCHEMAS = False

# STATIC
STATIC_URL = '/static'
STATIC_PATH = 'src/static/'

# mongo
MONGO_URI = ''
MONGO_DB = ''
