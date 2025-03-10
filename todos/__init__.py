from flask import Flask, render_template

from todos import todo, auth


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(DEBUG=True, SECRET_KEY='MY_SECRET_KEY')

    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
