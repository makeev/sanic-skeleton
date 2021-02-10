from tortoise import Model, fields


class User(Model):
    name = fields.CharField(max_length=100)

    def __str__(self):
        return self.name
