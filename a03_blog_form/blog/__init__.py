from flask import Flask, render_template, request
from datetime import datetime

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        heading = 'index page!'
        now = datetime.now()
        return render_template('index.html', heading=heading, now=now)

    @app.route('/<string:name>', methods=['POST'])
    def test(name):
        name = name.capitalize()
        hobbies = request.form.get('hobbies').split(',')
        return render_template('test.html', name=name, hobbies=hobbies)

    return app
