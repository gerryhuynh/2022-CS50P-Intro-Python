from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(100)
    assert jar.capacity == 100
    jar = Jar(0)
    assert jar.capacity == 0

    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(6)
    assert jar.size == 11

    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    jar.withdraw(6)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.withdraw(2)