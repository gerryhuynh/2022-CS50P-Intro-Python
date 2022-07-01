from bank import value

def test_lowercase():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("what's up") == 100

def test_uppercase():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("What's up") == 100

def test_nonletter():
    assert value("12345") == 100
    assert value("!@#$") == 100
    assert value("") == 100