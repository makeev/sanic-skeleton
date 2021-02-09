# DB
TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.asyncpg',
            "credentials": {
                "user": "user2",
                "password": "user2",
                "host": "localhost",
                "port": "5432",
                "database": "sanic_db"
            },
            "minsize": 1,
            "maxsize": 1
        }
    },
    "apps": {
        "models": {
            "models": ["project.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    'use_tz': False,
    'timezone': 'UTC'
}
# create empty database on init
GENERATE_SCHEMAS = True

# STATIC
STATIC_URL = '/static'
STATIC_PATH = 'src/static/'
