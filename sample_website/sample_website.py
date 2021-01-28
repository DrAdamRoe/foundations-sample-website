from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/hallo')
def hallo():
    return 'Test Route'

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
