from umongo import Document, fields

from app import get_app

app = get_app()


@app.ctx.umongo.register
class User(Document):
    name = fields.StringField()

    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()

    class Meta:
        collection_name = 'users'
