# from email.policy import default
# from click import password_option
from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    'skam',
    host = 'localhost',
    port = '5432',
    user = 'adi',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Instagram(BaseModel):
    user_name = CharField(max_length=255, null=False)
    password = CharField(max_length=255, null=False)
    date = DateField(default=datetime.now)

    def __repr__(self):
        return self.user_name

# db.create_tables([Instagram])

db.close