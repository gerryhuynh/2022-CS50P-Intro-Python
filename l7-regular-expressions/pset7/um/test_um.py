from um import count


def test_1um():
    assert count("um") == 1
    assert count("Um") == 1


def test_um_punctuation():
    assert count("um?") == 1
    assert count("um.") == 1


def test_um_in_word():
    assert count("yummy") == 0
    assert count("yum") == 0


def test_multiple_um():
    assert count("Um, thanks, um...") == 2