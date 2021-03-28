from covid_full_stack_app.website import app

# add 2nd level of directory hierarchy so tests run sucessfully from root.
app.config['DATABASE_FILE'] = 'covid_full_stack_app/' + app.config['DATABASE_FILE']  # noqa: E501


# a functional test
# instead of checking if a function() does it's job alone, this will check
# the entire response from the flask app, including the http status code.
def test_index():
    # create a version of our website that we can use for testing
    with app.test_client() as test_client:
        # mimic a browser: 'GET /', as if you visit the site
        response = test_client.get('/')

        # check that the HTTP response is a success
        assert response.status_code == 200

        # Store the contents of the html response in a local variable.
        # This should be a string with the same content as the file index.html
        html_content = response.data.decode()

        assert "<html>" in html_content


def test_get():
    # create a version of our website that we can use for testing
    with app.test_client() as test_client:
        # mimic our javascript "get" function
        response = test_client.get('/api/meetings/all')

        # check that the HTTP response is a success
        assert response.status_code == 200
