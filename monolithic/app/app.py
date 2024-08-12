# Simple monolithic application which has 2 services. A Hello service and a Hi service.

from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello!"


@app.route('/hi')
def hi():
    return "Hi!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
