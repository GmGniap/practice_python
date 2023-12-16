from w5_demo import get_short_country_code, get_full_country_name
from w5_class_demo import check_number_format


def test_check_number():
    assert check_number_format(-1) == "Negative"


"""
def test_country_code():
    short_code = get_short_country_code("paing")
    assert short_code == "MM"

    full_name = get_full_country_name(short_code)
    assert full_name == "Myanmar"
"""
