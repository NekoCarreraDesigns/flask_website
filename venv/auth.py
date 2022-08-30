from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/log_in')
def log_in():
    return "<p>Login</p>"


@auth.route('log_out')
def log_out():
    return "<p>logout</p>"


@auth.route('/sign_up')
def sign_up():
    return "<p>Sign Up</p>"
