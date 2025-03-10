from flask import Flask, render_template

from todos import todo, auth
from todos.db import get_db
from . import models


def create_app():
    app = Flask(__name__)

    # Configuración del poyecto
    app.config.from_mapping(
        DEBUG=False,
        SECRET_KEY='devtod',
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"
    )

    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    database = get_db()
    database.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        database.create_all()

    return app
