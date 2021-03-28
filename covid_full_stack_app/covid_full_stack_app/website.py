from os import getenv
from shutil import copyfile

from flask import Flask, request, Response
from flask import render_template
from flask import jsonify
from covid_full_stack_app.controllers.database_helpers import connect_to_database  # noqa: E501
from covid_full_stack_app.controllers.database_helpers import close_conection_to_database  # noqa: E501
from covid_full_stack_app.controllers.database_helpers import change_database
from covid_full_stack_app.controllers.database_helpers import query_database

app = Flask(__name__)

# This is a terrible example of how to configure a flask.
# this type of configuration should be done in a separate file,
# using environment variables. The code is written this way for
# relative ease of reading - but the code gets out of hand very
# quickly if you follow this approach.

# local file for testing purposes
app.config['DATABASE_FILE'] = 'covid_full_stack_app/data/covid_app.sqlite'

# hack to run with sqlite on app engine: if the code is run on app engine,
# this will copy the existing database to a writeable tmp directory.
# note that it will get overwritten every time you deploy! a production-ready
# approach is to store the file long-term on google cloud storage,
# or, better yet, use fully managed  relational database management software
# via Cloud SQL.
if getenv('GAE_ENV', '').startswith('standard'):
    app_engine_path = "/tmp/covid_app.sqlite"
    copyfile(app.config['DATABASE_FILE'], app_engine_path)
    app.config['DATABASE_FILE'] = app_engine_path
else:
    pass


# the index route. Note that there is no "logic" here anymore.
@app.route('/')
def index():
    return render_template('index.html', page_title="Covid Diary")


# this is an API route which will create a new "meeting",
# or, as it is coded here: add a name to the database. Note that
# only the HTTP POST method is allowed, which corresponds to a "Create"
# request, or an SQL INSERT command.
@app.route('/api/meetings', methods=['POST'])
def create_meeting():
    try:
        name = request.form.get('name')
        # app.logger.info(name)
        # turn this into an SQL command. For example:
        # "Adam" --> "INSERT INTO Meetings (name) VALUES("Adam");"
        sql_insert = "INSERT INTO Meetings (name) VALUES (\"{name}\");".format(
            name=name)

        # connect to the database with the filename configured above
        # returning a 2-tuple that contains a connection and cursor object
        # --> see file database_helpers for more
        database_tuple = connect_to_database(app.config["DATABASE_FILE"])

        # now that we have connected, add the new meeting (insert a row)
        # --> see file database_helpers for more
        change_database(database_tuple[0], database_tuple[1], sql_insert)

        # We will respond only with an HTTP Status code, without any HTML
        # The status code 201 means "created": a row was added to the database
        return Response(status=201)
    except Exception:
        # something bad happended. Return an error page and a 500 error
        error_code = 500
        return render_template('error.html', page_title=error_code), error_code


# this is an API route which will do what the URI says: it will return all
# of the meetings in the database. Note that only the HTTP GET method is
# allowed, corresponding to a READ request, or a SQL SELECT.
@app.route('/api/meetings/all', methods=['GET'])
def get_all_meetings():
    try:
        # connect to the database
        database_tuple = connect_to_database(app.config["DATABASE_FILE"])

        # first, define query to get all meetings:
        sql_query = "SELECT * FROM Meetings;"

        # query the database, by passinng the database cursor and query,
        # we expect a list of tuples corresponding to all rows in the database
        query_response = query_database(database_tuple[1], sql_query)

        # close the database connection
        close_conection_to_database(database_tuple[0])

        # return the result of the query to the frontend,  in JSON format
        return jsonify(query_response)

    except Exception:
        # something bad happended. Return an error page and a 500 error
        error_code = 500
        return render_template('error.html', page_title=error_code), error_code


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
