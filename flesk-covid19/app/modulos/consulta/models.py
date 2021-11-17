import peewee
from app.modulos.core import models as core

class Exames(core.BaseModel):

  cpf = peewee.CharField(unique=True)
  name = peewee.CharField()
  gender = peewee.CharField()
  age = peewee.IntegerField()
  email = peewee.CharField()
  tell = peewee.CharField()
  district = peewee.CharField()
  group_risk = peewee.CharField()
  symptoms = peewee.TextField()
  status = peewee.IntegerField(default=0)