from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/log_in')
def log_in():
    return render_template("log_in.html", boolean=True)


@auth.route('log_out')
def log_out():
    return "<p>logout</p>"


@auth.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")
