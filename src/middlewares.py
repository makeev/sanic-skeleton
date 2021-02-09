from app import get_app

app = get_app()


@app.middleware("request")
async def context_middleware(request):
    request.ctx.foo = 'bar'


@app.middleware("response")
async def response_middleware(request, response):
    response.headers['my-header'] = '1'
