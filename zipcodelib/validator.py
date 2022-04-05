import re


VALIDATION_PATTERN = r'^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$'
AREAS_WITH_SINGLE_DIGIT_DISTRICTS = ["BR", "FY", "HA", "HD", "HG", "HR", "HS", "HX", "JE", "LD", "SM", "SR",
                                     "WC", "WN", "ZE"]
AREAS_WITH_DOUBLE_DIGITS_DISTRICTS = ["AB", "LL", "SO"]
AREAS_WITH_DISTRICT_ZERO = ["BL", "BS", "CM", "CR", "FY", "HA", "PR", "SL", "SS"]
CENTRAL_LONDON_DISTRICTS = ['EC1', 'EC2', 'EC3', 'EC4', 'SW1', 'W1', 'WC1', 'WC2', 'E1W', 'N1C', 'N1P', 'NW1W', 'SE1P']


def _check_validation_regex(zipcode: str) -> bool:
    """
    Checks if zipcode string complies with the validation regex

    :param zipcode: Postcode string
    :return: bool
    """
    return re.match(VALIDATION_PATTERN, zipcode) is not None


def _split_zipcode(zipcode: str) -> (str, str, str, str):
    """
    Extract the postcode field from the zipcode.

    :param zipcode: Postcode string
    :return: Area, District, Sector, Unit
    """

    outward_code = zipcode[:-4]
    area = outward_code[:2]
    district = outward_code[2:]

    inward_code = zipcode[-3:]
    sector = inward_code[0]
    unit = inward_code[1:]
    return area, district, sector, unit


def _check_areas_with_only_single_digit_districts(area: str, district: str) -> bool:
    """
    Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE (although WC
    is always subdivided by a further letter, e.g. WC1A)

    :param area: Postcode area
    :param district: Postcode district
    :return: Is valid?
    """
    if area == "WC" and len(district) == 2 and re.match(r'[0-9][A-Z].*', district) is not None:
        return True
    elif area != "WC" and len(district) == 1 and district[0].isdigit():
        return True
    else:
        return False


def _check_areas_with_only_double_digit_districts(district: str) -> bool:
    """
    Areas with only double-digit districts: AB, LL, SO

    :param district: Postcode district
    :return: Is valid?
    """
    return len(district) == 2 and district.isdigit()


def is_valid(zipcode: str) -> bool:
    """
    Checks if the Postcode is valid.

    :param zipcode: Postcode string
    :return: bool
    """

    if not _check_validation_regex(zipcode):
        return False

    (area, district, sector, unit) = _split_zipcode(zipcode)

    if area in AREAS_WITH_SINGLE_DIGIT_DISTRICTS:
        return _check_areas_with_only_single_digit_districts(area, district)

    if area in AREAS_WITH_DOUBLE_DIGITS_DISTRICTS:
        return _check_areas_with_only_double_digit_districts(district)

    # Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS
    if district == '0' and area not in AREAS_WITH_DISTRICT_ZERO:
        return False

    # BS is the only area to have both a district 0 and a district 10
    if district == '10' and area != 'BS' and area in AREAS_WITH_DISTRICT_ZERO:
        return False

    # The following central London single-digit districts have been further divided by inserting a letter after the
    # digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2 and parts of E1 (E1W), N1 (N1C and N1P),
    # NW1 (NW1W) and SE1 (SE1P).
    for prefix in CENTRAL_LONDON_DISTRICTS:
        if zipcode.startswith(prefix):
            if not district[-1].isalpha():
                return False

    # The letters Q, V and X are not used in the first position.
    if zipcode[0] in ['Q', 'V', 'X']:
        return False

    # The letters I, J and Z are not used in the second position.
    if zipcode[1] in ['I', 'J', 'Z']:
        return False

    # The only letters to appear in the third position are A, B, C, D, E, F, G, H, J, K, P, S, T, U and W when the
    # structure starts with A9A.
    third_position = zipcode[2]
    if re.match(r'[A-Z][0-9][A-Z].*', zipcode) is not None and third_position not in ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                                                                      'H', 'J', 'K', 'P', 'S', 'T', 'U', 'W']:
        return False

    # The only letters to appear in the fourth position are A, B, E, H, M, N, P, R, V, W, X and Y when the structure
    # starts with AA9A.
    fourth_position = zipcode[3]
    if re.match(r'[A-Z]{2}[0-9][A-Z].*', zipcode) is not None and fourth_position not in ['A', 'B', 'E', 'H', 'M', 'N',
                                                                                          'P', 'R', 'V', 'W', 'X', 'Y']:
        return False

    # The final two letters do not use C, I, K, M, O or V, so as not to resemble digits or each other when handwritten.
    if bool(set(unit) & {'C', 'I', 'K', 'M', 'O', 'V'}):
        return False

    return True
