from sanic import response
from webargs_sanic.sanicparser import SanicParser, parser, HandleValidationError

from app import get_app


app = get_app()


class ValidationParser(SanicParser):
    DEFAULT_VALIDATION_STATUS = 400


# Return validation errors as JSON
@app.exception(HandleValidationError)
async def handle_validation_error(request, err):
    return response.json({"errors": err.exc.messages}, status=400)


parser = ValidationParser()
use_args = parser.use_args
use_kwargs = parser.use_kwargs
