from sample_website.sample_website import hello_world


def test_response():
    assert hello_world() == 'Hello, Flask!'

