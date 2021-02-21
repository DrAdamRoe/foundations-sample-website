from sample_website.website import hello_world


def test_sample_website():
    assert hello_world() == '<h1>Hello, Flask!</h1>'
