import os

USE_TZ = False
TIMEZONE = 'UTC'
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

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
            "minsize": 1,
            "maxsize": 1
        }
    },
    "apps": {
        "models": {
            "models": [
                "project.models",
            ],
            "default_connection": "default",
        },
    },
    'use_tz': USE_TZ,
    'timezone': TIMEZONE
}

REDIS_URL = 'redis://localhost'

# create empty database on init
GENERATE_SCHEMAS = True

# STATIC
STATIC_URL = '/static'
STATIC_PATH = 'src/static/'
