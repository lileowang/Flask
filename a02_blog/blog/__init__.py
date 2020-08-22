from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        return 'index page'

    @app.route('/<string:name>')
    def test(name):
        name = name.capitalize()
        return f'hello, {name}'

    return app
