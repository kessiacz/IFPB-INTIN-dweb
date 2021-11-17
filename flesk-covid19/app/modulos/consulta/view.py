import peewee
from flask import Blueprint, render_template, request, redirect, url_for

from .models import Exames
from .forms import CategoryForm

cons = Blueprint("cons", __name__, url_prefix='/consultas')

@cons.route("/", methods=['GET'])
def consultaspage():
  exames = Exames.select().order_by(Exames.status)
  return render_template('table.html', exames=exames)

@cons.route("/cadastro", methods=['GET'])
def conspage():
  exames = Exames.select()
  form = CategoryForm(request.form)
  return render_template('consulta.html', form=form, exames=exames)

@cons.route('/atualizar/<int:exame_id>/<int:status>', methods=['GET'])
def update(exame_id, status):
  exame = Exames.get(id=exame_id)
  exame.status = status
  exame.save()
  return redirect(url_for('cons.consultaspage'))

@cons.route('/formulario', methods=['POST'])
def formPost():
  form = CategoryForm(request.form)
  if form.validate_on_submit():

    try:
      Exames.create(cpf=form.cpf.data, name=form.name.data, gender=form.gender.data, age=form.age.data,email=form.email.data, tell= form.tell.data, district= form.district.data, group_risk= form.group_risk.data, symptoms= form.symptoms.data)
    except peewee.IntegrityError:
      return render_template('enviado.html', error='Paciente já cadastrado!')
  
  else:
      return render_template('consulta.html', form=form, error='ERROR')

  return render_template('enviado.html', form=form)