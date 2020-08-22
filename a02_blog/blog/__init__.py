from flask import Flask, render_template
from datetime import datetime

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        heading = 'index page'
        now = datetime.now()
        return render_template('index.html', heading=heading, now=now)

    @app.route('/<string:name>')
    def test(name):
        name = name.capitalize()
        days = ['mon', 'tue', 'wed']
        return render_template('test.html', name=name, days=days)

    return app
