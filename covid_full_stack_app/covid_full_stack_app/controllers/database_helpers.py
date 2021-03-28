# connect to the database and run some SQL

# import the python library for SQLite
import sqlite3


# this function will connect you to the database. It will return a tuple
# with two elements:
#  - a "connection" object, which will be necessary to later close the database
#  - a "cursor" object, which will neccesary to run SQL queries.
# This function is like opening a file for reading and writing.
# this function takes one argument, a string, the path to a database file.
def connect_to_database(database_filename):
    # connect to the database file, and create a connection object
    try:
        db_connection = sqlite3.connect(database_filename)
    except sqlite3.DatabaseError:
        print("Error while connecting to database file {filename}".format(
            filename=database_filename))

    # create a database cursor object, neccesary to use SQL
    db_cursor = db_connection.cursor()

    return db_connection, db_cursor


# close the connection to the database, like closing a file.
def close_conection_to_database(db_connection):
    db_connection.close()
    return


# This function will change either the structure or contents of your database.
# This expects SQL commands like "CREATE" or "INSERT"
def change_database(db_connection, db_cursor, sql_command):
    try:
        db_cursor.execute(sql_command)
    except sqlite3.DatabaseError:
        print("tried to execute the folllwing SQL, but failed:", sql_command)

    # commit changes - like with git.
    db_connection.commit()
    return


# this function will run any SQL query and return a list of tuples,
# where each tuple represents a row in the database.
# the intent here is to use this for seeing what is inside the database.
# SQL commands like "SELECT" are expected here
def query_database(db_cursor, sql_query):
    try:
        db_cursor.execute(sql_query)
    except sqlite3.DatabaseError:
        print("tried to execute the folllwing SQL, but failed:", sql_query)

    # list of tuples, where each tuple represents a row in the database
    query_response = db_cursor.fetchall()

    return query_response
