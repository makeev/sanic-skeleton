from tortoise import Model, fields


class User(Model):
    name = fields.CharField(max_length=100)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name
