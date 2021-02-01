from sample_website.sample_website import hello_world


def test_sample_website():
    assert hello_world() == '<h1>Hello, Week 1!</h1>'

