import pytest
from zipcodelib import formatter

zipcodes_with_good_format = [
    ("EC1A 1BB", "EC1A 1BB"),
    ("W1A 0AX", "W1A 0AX"),
    ("M1 1AE", "M1 1AE"),
    ("B33 8TH", "B33 8TH"),
    ("CR2 6XH", "CR2 6XH"),
    ("DN55 1PT", "DN55 1PT"),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_with_good_format)
def test_formatter_with_zipcodes_with_good_format(zip_code, expected):
    assert formatter.str_format(zip_code) == expected


zipcodes_without_spaces = [
    ("EC1A1BB", "EC1A 1BB"),
    ("W1A0AX", "W1A 0AX"),
    ("M11AE", "M1 1AE"),
    ("B338TH", "B33 8TH"),
    ("CR26XH", "CR2 6XH"),
    ("DN551PT", "DN55 1PT"),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_without_spaces)
def test_formatter_with_zipcodes_without_spaces(zip_code, expected):
    assert formatter.str_format(zip_code) == expected


zipcodes_with_weird_characters = [
    ("EC1A-1BB", "EC1A 1BB"),
    ("W1A-0AX", "W1A 0AX"),
    ("M1-1AE", "M1 1AE"),
    ("B33-8TH", "B33 8TH"),
    ("CR2-6XH", "CR2 6XH"),
    ("DN55-1PT", "DN55 1PT"),

    ("EC1A/1BB", "EC1A 1BB"),
    ("W1A/0AX", "W1A 0AX"),
    ("M1/1AE", "M1 1AE"),
    ("B33/8TH", "B33 8TH"),
    ("CR2/6XH", "CR2 6XH"),
    ("DN55/1PT", "DN55 1PT"),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_with_weird_characters)
def test_formatter_with_zipcodes_with_weird_characters(zip_code, expected):
    assert formatter.str_format(zip_code) == expected


zipcodes_with_spaces_in_weird_places = [
    ("E C 1 A 1 B B", "EC1A 1BB"),
    ("W  1  A  0  A  X", "W1A 0AX"),
    ("M   1   1   A   E", "M1 1AE"),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_with_spaces_in_weird_places)
def test_formatter_with_zipcodes_with_spaces_in_weird_places(zip_code, expected):
    assert formatter.str_format(zip_code) == expected


def test_formatter_value_error():
    dummy_zipcode = "123"
    with pytest.raises(ValueError, match=r"Unable to format 123"):
        formatter.str_format(dummy_zipcode)
