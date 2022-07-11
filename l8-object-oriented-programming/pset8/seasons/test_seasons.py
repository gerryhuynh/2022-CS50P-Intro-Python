from datetime import date
import pytest
from seasons import age_in_minutes


def test_invalid_format():
    with pytest.raises(SystemExit):
        age_in_minutes("January 1, 2021")


def test_valid():
    assert age_in_minutes(str(date.today().replace(year = date.today().year - 1))) == "Five hundred twenty-five thousand, six hundred minutes"
    assert age_in_minutes(str(date.today().replace(year = date.today().year - 2))) == "One million, fifty-one thousand, two hundred minutes"


