import pytest
from zipcodelib import validator


normal_cases = [
    ("EC1A 1BB", True),
    ("W1A 0AX", True),
    ("M1 1AE", True),
    ("B33 8TH", True),
    ("CR2 6XH", True),
    ("DN55 1PT", True),
]


@pytest.mark.parametrize("zip_code, expected", normal_cases)
def test_validation_for_normal_cases(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_with_only_single_digit_districts_allowed = [
    # Single-digit districts
    ("BR9 9AA", True),
    ("FY9 9AA", True),
    ("HA9 9AA", True),
    ("HD9 9AA", True),
    ("HG9 9AA", True),
    ("HR9 9AA", True),
    ("HS9 9AA", True),
    ("HX9 9AA", True),
    ("JE9 9AA", True),
    ("LD9 9AA", True),
    ("SM9 9AA", True),
    ("SR9 9AA", True),
    ("WN9 9AA", True),
    ("ZE9 9AA", True),

    # Double-digit districts
    ("BR99 9AA", False),
    ("FY99 9AA", False),
    ("HA99 9AA", False),
    ("HD99 9AA", False),
    ("HG99 9AA", False),
    ("HR99 9AA", False),
    ("HS99 9AA", False),
    ("HX99 9AA", False),
    ("JE99 9AA", False),
    ("LD99 9AA", False),
    ("SM99 9AA", False),
    ("SR99 9AA", False),
    ("WC99 9AA", False),
    ("WN99 9AA", False),
    ("ZE99 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_with_only_single_digit_districts_allowed)
def test_validation_for_areas_with_only_single_digit_districts(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


wc_zipcodes = [
    # Alphanumeric district
    ("WC9A 9AA", True),
    # Numeric district
    ("WC9 9AA", False),
    # Alphabetic district
    ("WCAA 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", wc_zipcodes)
def test_validation_for_wc_area(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_with_only_double_digit_districts_allowed = [
    # Double-digit districts
    ("AB99 9AA", True),
    ("LL99 9AA", True),
    ("SO99 9AA", True),

    # Double-digit districts
    ("AB9 9AA", False),
    ("LL9 9AA", False),
    ("SO9 9AA", False),

    # Alphanumeric districts
    ("AB9A 9AA", False),
    ("LL9A 9AA", False),
    ("SO9A 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_with_only_double_digit_districts_allowed)
def test_validation_for_areas_with_only_double_digit_districts(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_with_district_zero_allowed_but_not_ten = [
    # Allowed district 0
    ("BL0 9AA", True),
    ("CM0 9AA", True),
    ("CR0 9AA", True),
    ("FY0 9AA", True),
    ("HA0 9AA", True),
    ("PR0 9AA", True),
    ("SL0 9AA", True),
    ("SS0 9AA", True),

    # Forbidden district 10
    ("BL10 9AA", False),
    ("CM10 9AA", False),
    ("CR10 9AA", False),
    ("FY10 9AA", False),
    ("HA10 9AA", False),
    ("PR10 9AA", False),
    ("SL10 9AA", False),
    ("SS10 9AA", False),

    # Forbidden district 0
    ("AA0 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_with_district_zero_allowed_but_not_ten)
def test_validation_for_areas_with_district_zero_allowed_but_not_ten(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_with_district_zero_and_ten_allowed = [
    ("BS0 9AA", True),
    ("BS10 9AA", True),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_with_district_zero_and_ten_allowed)
def test_validation_for_areas_with_district_zero_and_ten_allowed(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_first_position_forbidden_characters = [
    # Forbidden letters for first position
    ("QA9A 9AA", False),
    ("VA9A 9AA", False),
    ("XA9A 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_first_position_forbidden_characters)
def test_validation_first_position(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


central_london_districts = [
    # Last district character is letter
    ("EC1A 9AA", True),
    ("EC2A 9AA", True),
    ("EC3A 9AA", True),
    ("EC4A 9AA", True),
    ("SW1A 9AA", True),
    ("W1A 9AA", True),
    ("WC1A 9AA", True),
    ("WC2A 9AA", True),
    ("E1W 9AA", True),
    ("N1C 9AA", True),
    ("N1P 9AA", True),
    ("NW1W 9AA", True),
    ("SE1P 9AA", True),

    # Last district character is digit
    ("EC19 9AA", False),
    ("EC29 9AA", False),
    ("EC39 9AA", False),
    ("EC49 9AA", False),
    ("SW19 9AA", False),
    ("W19 9AA", False),
    ("WC19 9AA", False),
    ("WC29 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", central_london_districts)
def test_validation_central_london_districts(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_second_position_forbidden_characters = [
    # Forbidden letters for second position
    ("AI9A 9AA", False),
    ("AJ9A 9AA", False),
    ("AZ9A 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_second_position_forbidden_characters)
def test_validation_second_position(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_third_position = [
    # Allowed letters for third position
    ("A9A 9AA", True),
    ("A9B 9AA", True),
    ("A9C 9AA", True),
    ("A9D 9AA", True),
    ("A9E 9AA", True),
    ("A9F 9AA", True),
    ("A9G 9AA", True),
    ("A9H 9AA", True),
    ("A9J 9AA", True),
    ("A9K 9AA", True),
    ("A9P 9AA", True),
    ("A9S 9AA", True),
    ("A9T 9AA", True),
    ("A9U 9AA", True),
    ("A9W 9AA", True),

    # Forbidden letters for third position
    ("A9I 9AA", False),
    ("A9L 9AA", False),
    ("A9M 9AA", False),
    ("A9N 9AA", False),
    ("A9O 9AA", False),
    ("A9Q 9AA", False),
    ("A9R 9AA", False),
    ("A9V 9AA", False),
    ("A9X 9AA", False),
    ("A9Y 9AA", False),
    ("A9Z 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_third_position)
def test_validation_third_position(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_fourth_position = [
    # Allowed letters for fourth position
    ("AA9A 9AA", True),
    ("AA9B 9AA", True),
    ("AA9E 9AA", True),
    ("AA9H 9AA", True),
    ("AA9M 9AA", True),
    ("AA9N 9AA", True),
    ("AA9P 9AA", True),
    ("AA9R 9AA", True),
    ("AA9V 9AA", True),
    ("AA9W 9AA", True),
    ("AA9X 9AA", True),
    ("AA9Y 9AA", True),

    # Forbidden letters for fourth position
    ("AA9C 9AA", False),
    ("AA9D 9AA", False),
    ("AA9F 9AA", False),
    ("AA9G 9AA", False),
    ("AA9I 9AA", False),
    ("AA9J 9AA", False),
    ("AA9L 9AA", False),
    ("AA9K 9AA", False),
    ("AA9O 9AA", False),
    ("AA9Q 9AA", False),
    ("AA9S 9AA", False),
    ("AA9T 9AA", False),
    ("AA9U 9AA", False),
    ("AA9Z 9AA", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_fourth_position)
def test_validation_fourth_position(zip_code, expected):
    assert validator.is_valid(zip_code) == expected


zipcodes_invalid_units = [
    # Forbidden letters for Postcode unit
    ("A9A 9CA", False),
    ("A9A 9IA", False),
    ("A9A 9KA", False),
    ("A9A 9MA", False),
    ("A9A 9OA", False),
    ("A9A 9VA", False),
    ("A9A 9AC", False),
    ("A9A 9AI", False),
    ("A9A 9AK", False),
    ("A9A 9AM", False),
    ("A9A 9AO", False),
    ("A9A 9AV", False),
]


@pytest.mark.parametrize("zip_code, expected", zipcodes_invalid_units)
def test_validation_with_invalid_unit(zip_code, expected):
    assert validator.is_valid(zip_code) == expected
