from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/works')
def first_page():
    return render_template('works.html', page_title="Works")


@app.route('/contact')
def second_page():
    return render_template('contact.html', page_title="Let's talk")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
