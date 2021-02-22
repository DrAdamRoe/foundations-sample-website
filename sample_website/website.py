from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, Humam!</h1>'


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
