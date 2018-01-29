from peewee import *


db = SqliteDatabase('challenges.db')


class Challenge(Model):
    name = CharField(maxlength=100)
    language = CharField(maxlength=100)
    steps = IntegerField(default=1)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Challenge]), safe = True)
