from flask import Flask, request
from flask import render_template
from covid_app.controllers.database_helpers import connect_to_database
from covid_app.controllers.database_helpers import close_conection_to_database
from covid_app.controllers.database_helpers import change_database
from covid_app.controllers.database_helpers import query_database


app = Flask(__name__)

# This is an example of how to configure a flask.
app.config['DATABASE_FILE'] = 'data/covid_app.sqlite'


@app.route('/')
def index():
    return render_template('index.html', page_title="Covid Diary")


@app.route('/create', methods=['POST'])
def create_meeting():
    try:
        name = request.form.get('name')
        print("met:", name, "today")
        # turn this into an SQL command
        sql_insert = "INSERT INTO Meetings VALUES {name}".format(name=name)

        # connect to the database with the filename configured above
        # returning a 2-tuple that contains a connection and cursor object
        # --> see file database_helpers for more
        database_tuple = connect_to_database(app.config("DATABASE_FILE"))

        # now that we have connected, add the new meeting (insert a row)
        # --> see file database_helpers for more
        change_database(database_tuple[0], database_tuple[1], sql_insert)

        # now, get all of the meetings from the database, not just the new one.
        # first, define the query to get all meetings:
        sql_query = "FROM Meetings SELECT *"

        # query the database, by passinng the database cursor and query,
        # we expect a list of tuples corresponding to all rows in the database
        query_response = query_database(database_tuple[1], sql_query)

        close_conection_to_database(database_tuple[0])

        # In addition to HTML, we will respond with an HTTP Status code
        # The status code 201 means "created": a row was added to the database
        return render_template('index.html', page_title="Covid Diary",
                               meetings=query_response), 201
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
