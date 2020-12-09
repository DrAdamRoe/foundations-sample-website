from flasky import hello_world


def test_response():
    assert hello_world() == 'Hello, Flask!'
