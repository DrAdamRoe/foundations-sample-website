from os import getenv
from shutil import copyfile

from flask import Flask, request
from flask import render_template
from controllers.database_helpers import connect_to_database
from controllers.database_helpers import close_conection_to_database
from controllers.database_helpers import change_database
from controllers.database_helpers import query_database

from datetime import date, timedelta
date = date.today()
twoWeeks = timedelta(weeks=2)
dateTwoWeeks = date - twoWeeks

app = Flask(__name__)

# This is a terrible example of how to configure a flask.
# this type of configuration should be done in a separate file,
# using environment variables. The code is written this way for
# relative ease of reading - but the code gets out of hand very
# quickly if you follow this approach.

# local file for testing purposes
app.config['DATABASE_FILE'] = 'covid_app/data/covid_app.sqlite'

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


@app.route('/')
def index():
    try:
        database_tuple = connect_to_database(app.config["DATABASE_FILE"])
        # now, get all of the meetings from the database, not just the new one.
        # first, define the query to get all meetings:
        sql_query_recent = "SELECT * FROM Meetings WHERE date > \"{dateTwoWeeks}\" ORDER BY date DESC;".format(
            dateTwoWeeks=dateTwoWeeks)
        sql_query_general = "SELECT * FROM Meetings ORDER BY date DESC;"

        sql_query_contacts = "SELECT * FROM Contacts;"
        sql_query_locations = "SELECT * FROM Locations;"

        # query the database, by passinng the database cursor and query,
        # we expect a list of tuples corresponding to all rows in the database
        query_response_recent = query_database(
            database_tuple[1], sql_query_recent)
        query_response_general = query_database(
            database_tuple[1], sql_query_general)

        query_response_contacts = query_database(
            database_tuple[1], sql_query_contacts)
        query_response_locations = query_database(
            database_tuple[1], sql_query_locations)

        close_conection_to_database(database_tuple[0])

        # In addition to HTML, we will respond with an HTTP Status code
        # The status code 201 means "created": a row was added to the database
        return render_template('index.html', page_title="Covid Diary",
                               meetings_recent=query_response_recent, meetings_general=query_response_general, contacts=query_response_contacts, locations=query_response_locations, msg_color=msg_color), 201
    except Exception:
        # something bad happended. Return an error page and a 500 error
        error_code = 500
        return render_template('error.html', page_title=error_code), error_code


@app.route('/add_contact', methods=['POST'])
def add_new_contact():
    msg_color = "green"
    msg = "Added :)"
    new_contact = request.form.get('new_contact')
    database_tuple = connect_to_database(app.config["DATABASE_FILE"])
    if new_contact != "":
        sql_insert_contact = "INSERT INTO Contacts (name) VALUES (\"{new_contact}\");".format(
            new_contact=new_contact)

        change_database(database_tuple[0], database_tuple[1], sql_insert_contact)
    else:
        msg = "Nooooo :( You forgot to write the new contact details into the box"
        msg_color = "red"

    sql_query_recent = "SELECT * FROM Meetings WHERE date > \"{dateTwoWeeks}\" ORDER BY date DESC;".format(
        dateTwoWeeks=dateTwoWeeks)
    sql_query_general = "SELECT * FROM Meetings ORDER BY date DESC;"

    sql_query_contacts = "SELECT * FROM Contacts;"
    sql_query_locations = "SELECT * FROM Locations;"

    query_response_recent = query_database(
        database_tuple[1], sql_query_recent)
    query_response_general = query_database(
        database_tuple[1], sql_query_general)

    query_response_contacts = query_database(
        database_tuple[1], sql_query_contacts)
    query_response_locations = query_database(
        database_tuple[1], sql_query_locations)

    close_conection_to_database(database_tuple[0])

    return render_template('index.html', page_title="Covid Diary",
                        meetings_recent=query_response_recent, meetings_general=query_response_general, contacts=query_response_contacts, locations=query_response_locations, msg=msg, msg_color=msg_color), 201


@app.route('/add_location', methods=['POST'])
def add_new_location():
    msg_color = "green"
    msg = "Added :)"
    new_location = request.form.get('new_location')
    database_tuple = connect_to_database(app.config["DATABASE_FILE"])
    if new_location != "":
        sql_insert_location = "INSERT INTO Locations (location) VALUES (\"{new_location}\");".format(
            new_location=new_location)

        change_database(database_tuple[0], database_tuple[1], sql_insert_location)
    else:
        msg = "Nooooo :( You forgot to write the new location details into the box"
        msg_color = "red"

    sql_query_recent = "SELECT * FROM Meetings WHERE date > \"{dateTwoWeeks}\" ORDER BY date DESC;".format(
        dateTwoWeeks=dateTwoWeeks)
    sql_query_general = "SELECT * FROM Meetings ORDER BY date DESC;"

    sql_query_contacts = "SELECT * FROM Contacts;"
    sql_query_locations = "SELECT * FROM Locations;"

    query_response_recent = query_database(
        database_tuple[1], sql_query_recent)
    query_response_general = query_database(
        database_tuple[1], sql_query_general)

    query_response_contacts = query_database(
        database_tuple[1], sql_query_contacts)
    query_response_locations = query_database(
        database_tuple[1], sql_query_locations)

    close_conection_to_database(database_tuple[0])

    return render_template('index.html', page_title="Covid Diary",
                           meetings_recent=query_response_recent, meetings_general=query_response_general, contacts=query_response_contacts, locations=query_response_locations, msg=msg), 201

@app.route('/create', methods=['POST'])
def create_meeting():
    try:
        name = request.form.get('name')
        location = request.form.get('location')
        # app.logger.info(name)
        # turn this into an SQL command. For example:
        # "Adam" --> "INSERT INTO Meetings (name) VALUES("Adam");"
        sql_insert = "INSERT INTO Meetings (name, date, location) VALUES (\"{name}\", \"{date}\", \"{location}\");".format(
            name=name, date=date, location=location)

        # connect to the database with the filename configured above
        # returning a 2-tuple that contains a connection and cursor object
        # --> see file database_helpers for more
        database_tuple = connect_to_database(app.config["DATABASE_FILE"])

        # now that we have connected, add the new meeting (insert a row)
        # --> see file database_helpers for more
        change_database(database_tuple[0], database_tuple[1], sql_insert)

        # now, get all of the meetings from the database, not just the new one.
        # first, define the query to get all meetings:
        sql_query_recent = "SELECT * FROM Meetings WHERE date > \"{dateTwoWeeks}\" ORDER BY date DESC;".format(
            dateTwoWeeks=dateTwoWeeks)
        sql_query_general = "SELECT * FROM Meetings ORDER BY date DESC;"

        sql_query_contacts = "SELECT * FROM Contacts;"
        sql_query_locations = "SELECT * FROM Locations;"

        # query the database, by passinng the database cursor and query,
        # we expect a list of tuples corresponding to all rows in the database
        query_response_recent = query_database(
            database_tuple[1], sql_query_recent)
        query_response_general = query_database(
            database_tuple[1], sql_query_general)

        query_response_contacts = query_database(
            database_tuple[1], sql_query_contacts)
        query_response_locations = query_database(
            database_tuple[1], sql_query_locations)

        close_conection_to_database(database_tuple[0])

        # In addition to HTML, we will respond with an HTTP Status code
        # The status code 201 means "created": a row was added to the database
        return render_template('index.html', page_title="Covid Diary",
                               meetings_recent=query_response_recent, meetings_general=query_response_general, contacts=query_response_contacts, locations=query_response_locations), 201
    except Exception:
        # something bad happended. Return an error page and a 500 error
        error_code = 500
        return render_template('error.html', page_title=error_code), error_code


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
