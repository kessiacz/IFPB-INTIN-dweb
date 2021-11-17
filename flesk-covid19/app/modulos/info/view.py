from flask import Blueprint, render_template

info = Blueprint('info', __name__)

@info.route("/info")
def infopage():
  return render_template('info.html')
