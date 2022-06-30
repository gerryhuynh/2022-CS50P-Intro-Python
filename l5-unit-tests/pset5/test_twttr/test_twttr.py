from twttr import shorten

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("CS50") == "CS50"


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("cs50") == "cs50"


def test_mixedcase():
    assert shorten("TwiTTEr") == "TwTTr"
    assert shorten("cS50") == "cS50"

def test_non_letters():
    assert shorten("") == ""
    assert shorten("123456") == "123456"
    assert shorten ("!@#$") == "!@#$"
    assert shorten("NULL") == "NLL"