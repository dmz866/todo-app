from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(DEBUG=True, SECRET_KEY='MY_SECRET_KEY')

    @app.route('/')
    def index():
        return 'Shi'

    return app
