from flask import Blueprint, render_template
from app.modulos.consulta.models import Exames
from peewee import *

main = Blueprint("main", __name__)

@main.route("/")
def homepage():
  exames = Exames.select(Exames.status, fn.COUNT(Exames.status).alias('ct')).group_by(Exames.status)
  boletim = {
    0: {
      "label": "Em analise",
      "count": 0
      },
    1: {
      "label": "Confirmados",
      "count": 0
      },
    2: {
      "label": "Descartados",
      "count": 0
      },
    3: {
      "label": "Obitos",
      "count": 0
      },
    4: {
      "label": "Internados",
      "count": 0
      },
    5: {
      "label": "Recuperados",
      "count": 0
      },
  }
  for c in exames:
    boletim[c.status]['count'] = c.ct
  print(exames.scalar())
  return render_template('index.html', boletim=boletim)
