from flask import Blueprint, render_template, request, redirect, url_for, g

from todos.routes.auth import login_required

from ..models import Todo, User
from todos.db import get_db

bp = Blueprint('todo', __name__, url_prefix='/todo')
db = get_db()


@bp.route('/list')
@login_required
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos=todos)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(g.user.id, title, desc)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))

    return render_template('todo/create.html')


def get_todo(todo_id):
    return Todo.query.get_or_404(todo_id)


@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(todo_id):
    todo = get_todo(todo_id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else False

        db.session.commit()
        return redirect(url_for('todo.index'))

    return render_template('todo/update.html', todo=todo)


@bp.route('/delete/<int:id>')
@login_required
def delete(todo_id):
    todo = get_todo(todo_id)
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('todo.index'))
