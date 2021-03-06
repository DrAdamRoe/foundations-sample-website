from week1.website import app


# our very first functional test
# instead of checking if a function() does it's job alone, this will check
# the entire response from the flask app, including the http status code.
def test_index():
    # create a version of our website that we can use for testing
    with app.test_client() as test_client:
        # mimic a browser: 'GET /', as if you visit the site
        response = test_client.get('/')

        # check that the HTTP response is a success
        assert response.status_code == 500

        # Store the contents of the html response in a local variable.
        # This should be a string with the same content as the file index.html
        html_content = response.data.decode()

        assert "<html>" in html_content
        # check that there is a header (ok, at least that there is an h1 tag)
        assert "<h1" in html_content
        # check that there is a at least two paragraph tags
        assert html_content.count("<p") >= 2
