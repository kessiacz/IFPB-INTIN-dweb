from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):
  
  cpf = StringField('CPF', validators=[DataRequired()])
  name = StringField('Nome', validators=[DataRequired()])
  gender = StringField('Gênero', validators=[DataRequired()])
  age = IntegerField('Idade', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired()])
  tell = StringField('Telefone', validators=[DataRequired()])
  district = StringField('Bairro', validators=[DataRequired()])
  group_risk = StringField('Grupo de Risco', validators=[DataRequired()])
  symptoms = StringField('Sintomas', validators=[DataRequired()])

