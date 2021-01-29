from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


def make_application():
    return app.wsgi_app