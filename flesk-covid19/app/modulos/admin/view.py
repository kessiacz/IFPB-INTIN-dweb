from flask import Blueprint, render_template, request, redirect, url_for

from .form import LoginForm

admin = Blueprint("admin", __name__)

@admin.route("/admin", methods=['GET','POST'])
def adminpage():
  form = LoginForm(request.form)
  if form.validate_on_submit():
    if form.user.data == 'admin' and form.senha.data == 'admin':
      return redirect(url_for('cons.consultaspage'))
    else:
      return render_template('admin.html', form=form, error = "Usuário ou senha incorretos")
  return render_template('admin.html', form=form)