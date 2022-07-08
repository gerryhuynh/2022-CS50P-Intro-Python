from numb3rs import validate


def test_format():
    assert validate("0.0.0.0") == True
    assert validate("0,0,0,0") == False
    assert validate("0") == False
    assert validate("0.0.0") == False
    assert validate("0.0.0.0.0") == False
    assert validate("") == False
    assert validate("...") == False


def test_num_range():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("275.3.6.28") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False


def test_invalid_chars():
    assert validate("a") == False
    assert validate("?!$") == False
    assert validate("a.a.a.a") == False
    assert validate("?.?.?.?") == False