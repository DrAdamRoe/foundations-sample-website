from sample_website2.sample_website import hello_flask


def test_response2():
    assert hello_flask() == 'Hello, Flask2!'

