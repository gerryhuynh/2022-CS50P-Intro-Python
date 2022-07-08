from multiprocessing.sharedctypes import Value
import pytest

from working import convert


def test_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_pm_to_am():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_dash():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_proper_format():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


# def test_format_1():
#     assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
#     assert convert(" 9:00 AM to 5:00 PM") == "09:00 to 17:00"
#     assert convert("9:00 AM to 5:00 PM ") == "09:00 to 17:00"

#     with pytest.raises(ValueError):
#         convert("9:00am to 5:00pm")
#     with pytest.raises(ValueError):
#         convert("9:00 am to 5:00 pm")
#     with pytest.raises(ValueError):
#         convert("9:00a.m. to 5:00p.m.")
#     with pytest.raises(ValueError):
#         convert("9:00 A.M. to 5:00 P.M.")

#     with pytest.raises(ValueError):
#         convert("09:00AM to 05:00PM")
#     with pytest.raises(ValueError):
#         convert("09:00am to 5:00pm")
#     with pytest.raises(ValueError):
#         convert("09:00 am to 5:00 pm")
#     with pytest.raises(ValueError):
#         convert("09:00a.m. to 5:00p.m.")
#     with pytest.raises(ValueError):
#         convert("09:00 A.M. to 5:00 P.M.")
    
#     with pytest.raises(ValueError):
#         convert("9:00AM - 5:00PM")
#     with pytest.raises(ValueError):
#         convert("9:00am - 5:00pm")
#     with pytest.raises(ValueError):
#         convert("9:00 am - 5:00 pm")
#     with pytest.raises(ValueError):
#         convert("9:00a.m. - 5:00p.m.")
#     with pytest.raises(ValueError):
#         convert("9:00 A.M. - 5:00 P.M.")

#     with pytest.raises(ValueError):
#         convert("09:00AM - 05:00PM")
#     with pytest.raises(ValueError):
#         convert("09:00am - 5:00pm")
#     with pytest.raises(ValueError):
#         convert("09:00 am - 5:00 pm")
#     with pytest.raises(ValueError):
#         convert("09:00a.m. - 5:00p.m.")
#     with pytest.raises(ValueError):
#         convert("09:00 A.M. - 5:00 P.M.")


# def test_format_2():
#     assert convert("9 AM to 5 PM") == "09:00 to 17:00"
#     assert convert(" 9 AM to 5 PM") == "09:00 to 17:00"
#     assert convert("9 AM to 5 PM ") == "09:00 to 17:00"
    

#     with pytest.raises(ValueError):
#         convert("9AM to 5PM")
#     with pytest.raises(ValueError):
#         convert("9am to 5pm")
#     with pytest.raises(ValueError):
#         convert("9 am to 5 pm")
#     with pytest.raises(ValueError):
#         convert("9a.m. to 5p.m.")
#     with pytest.raises(ValueError):
#         convert("9 A.M. to 5 P.M.")
    
#     with pytest.raises(ValueError):
#         convert("09AM to 05PM")
#     with pytest.raises(ValueError):
#         convert("09am to 05pm")
#     with pytest.raises(ValueError):
#         convert("09 am to 05 pm")
#     with pytest.raises(ValueError):
#         convert("09a.m. to 05p.m.")
#     with pytest.raises(ValueError):
#         convert("09 A.M. to 05 P.M.")

#     with pytest.raises(ValueError):
#         convert("9AM - 5PM")
#     with pytest.raises(ValueError):
#         convert("9am - 5pm")
#     with pytest.raises(ValueError):
#         convert("9 am - 5 pm")
#     with pytest.raises(ValueError):
#         convert("9a.m. - 5p.m.")
#     with pytest.raises(ValueError):
#         convert("9 A.M. - 5 P.M.")

#     with pytest.raises(ValueError):
#         convert("09AM - 05PM")
#     with pytest.raises(ValueError):
#         convert("09am - 05pm")
#     with pytest.raises(ValueError):
#         convert("09 am - 05 pm")
#     with pytest.raises(ValueError):
#         convert("09a.m. - 05p.m.")
#     with pytest.raises(ValueError):
#         convert("09 A.M. - 05 P.M.")


# def test_valid_time():
#     with pytest.raises(ValueError):
#         convert("12:60 AM to 5:00 PM")
#     with pytest.raises(ValueError):
#         convert("9:00 AM to 13:00 PM")