from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
db = get_db()


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, generate_password_hash(password))

        user_name = User.query.filter_by(username=username).first()

        if user_name is None:
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.login'))
        else:
            error = 'Username ya existe'
            flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            error = 'Credenciales incorrectas'
            flash(error)
        else:
            session.clear()
            session['user_id'] = user.id

            return redirect(url_for('todo.index'))

    return render_template('auth/login.html')
