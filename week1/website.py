from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first-page')
def first_page():
    return render_template('first-page.html', page_title="First Template Page")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
