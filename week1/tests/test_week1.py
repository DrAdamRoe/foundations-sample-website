from week1.sample_website import hello_world


def test_response():
    assert hello_world() == '<h1>Hello, Week 1!</h1>'

