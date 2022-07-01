from plates import is_valid


def test_char_placement():
    assert is_valid("AAA111") == True
    assert is_valid("AA1") == True
    assert is_valid("111AAA") == False
    assert is_valid("1") == False
    assert is_valid("A1") == False
    assert is_valid("AA11AA") == False


def test_length():
    assert is_valid("AAA111") == True
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("AAAA111") == False


def test_zero_start():
    assert is_valid("AA10") == True
    assert is_valid("AA01") == False


def test_alphanum():
    assert is_valid("!@#$%") == False
    assert is_valid("AA.11") == False
    assert is_valid(" ") == False
    assert is_valid("") == False