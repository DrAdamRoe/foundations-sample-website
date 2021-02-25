from color_check.website import app
from color_check.controllers.get_color_code import get_color_code


# test the  function we've written to check on the colors themselves
def test_get_color_code():
    # this test should pass right now
    assert get_color_code("blue") == "#0000ff"
    # the following test will fail at the beginning,
    # uncomment when you think you are finished!
    # assert get_color_code("red") == "#ff0000"


# our very first functional test
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


# check that there is a route at "/colors" which accepts a POST request
def test_colors():
    with app.test_client() as test_client:
        response = test_client.post('/color')
        assert response.status_code == 200
