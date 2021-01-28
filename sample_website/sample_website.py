from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.router('/test')
def test_route():
    return 'Test Route'

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
