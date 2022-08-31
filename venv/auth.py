from flask import Blueprint, render_template, request, flash
auth = Blueprint('auth', __name__)


@auth.route('/log_in', methods=['GET', 'POST'])
def log_in():
    return render_template("log_in.html", boolean=True)


@auth.route('log_out')
def log_out():
    return "<p>logout</p>"


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        FirstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be more than four characters', category='error')
        elif len(FirstName) < 2:
            flash('First name must be more than two characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 8:
            flash('Password needs to be eight characters long', category='error')
        else:
            flash('Account created', category='success')

    return render_template("sign_up.html")
