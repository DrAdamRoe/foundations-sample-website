from covid_app.website import app


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


# doesn't quite work as a test with this architecture; fix for next year. 
# # check that there is a route at "/create" which accepts a POST request
# def test_create():
#     with app.test_client() as test_client:

#         test_data = {'name': 'Adamliqhiohqeghwehg'}

#         response = test_client.post('/create', data=test_data)
#         assert response.status_code == 201
