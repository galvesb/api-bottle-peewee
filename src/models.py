from logging import DEBUG
from peewee import (
    Database,
    SqliteDatabase,
    Model,
    TextField,
    ForeignKeyField,
    DateTimeField,
    IntegerField,
)

db = SqliteDatabase("contas.db")

class BaseModel(Model):
    class Meta:
        database = db

class Mes(BaseModel):
    nome_mes = TextField(unique=True)