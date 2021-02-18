from sanic.exceptions import abort
from sanic.response import HTTPResponse

import settings


def raw_json(
        body,
        status=200,
        headers=None,
        content_type="application/json",
):
    return HTTPResponse(
        body,
        headers=headers,
        status=status,
        content_type=content_type,
    )


def token_required(f):
    async def wrapper(request, *args, **kwargs):
        token = request.headers.get('x-auth-token')
        if settings.AUTH_TOKEN and token != settings.AUTH_TOKEN:
            abort(403)

        return await f(request, *args, **kwargs)
    return wrapper
