from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("4/4") == 100


def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("a/b")


def test_convert_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"