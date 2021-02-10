"django like" async skeleton based on sanic framework and tortois orm

## how to run

```
./server.sh
```

or

```
cd src
sanic --debug app.app
```

## DB migrations

Upgrade to latest version
```
aerich upggrade
```
Downgrade to specified version
```
Usage: aerich downgrade [OPTIONS]

  Downgrade to specified version.

Options:
  -v, --version INTEGER  Specified version, default to last.  [default: -1]
  -h, --help             Show this message and exit.
> aerich downgrade

Success downgrade 1_202029051520102929_drop_column.json
```

Create new migration
```
> aerich migrate --name user_drop_column

Success migrate 1_202029051520102929_user_drop_column.json
```


## swagger docs

based on https://sanic-openapi.readthedocs.io/en/stable/

http://127.0.0.1:8000/swagger/
