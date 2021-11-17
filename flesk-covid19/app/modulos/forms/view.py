from flask import Blueprint, render_template

forms = Blueprint("forms", __name__)

@forms.route("/table")
def formspage():
  return render_template('table.html')
