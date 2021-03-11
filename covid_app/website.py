from flask import Flask, request
from flask import render_template
from covid_app.controllers.add_meeting import add_meeting
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="Covid Diary")


@app.route('/create', methods=['POST'])
def create_meeting():
    try:
        name = request.form.get('name')
        add_meeting(name)
        # In addition to HTML, we will respond with an HTTP Status code
        # The status code 201 means "created": a row was added to the database
        return render_template('index.html', page_title="Covid Diary"), 201
    except Exception:
        # something bad happended. Return an error page and a 500 error
        error_code = 500
        return render_template('error.html', page_title=error_code), error_code


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)


# next steps (Adam)
# - Create first table in database
# - Create connector, model, first controller
# - add comments, make assignment clear in code 
