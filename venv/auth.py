from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, try again", category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("log_in.html", user=current_user)


@auth.route('log_out')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('auth.log_in'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category='error')

        if len(email) < 4:
            flash('Email must be more than four characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be more than two characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 8:
            flash('Password needs to be eight characters long', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)
