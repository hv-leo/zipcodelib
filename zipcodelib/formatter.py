AA9A_PATTERN_STARTS_WITH = ['WC', 'EC1', 'EC2', 'EC3', 'EC4', 'NW1W', 'SE1P', 'SW1']
A9A_PATTERN_STARTS_WITH = ['E1', 'N1', 'W1']
A9_OR_A99_PATTERN_STARTS_WITH = ['B', 'E', 'G', 'L', 'M', 'N', 'S', 'W']


def str_format(zipcode: str) -> str:
    # Just consider alphanumeric characters.
    formatted_zipcode = ''.join(c for c in zipcode if c.isalnum())

    # Format: AA9A 9AA
    # Coverage: WC postcode area; EC1–EC4, NW1W, SE1P, SW1
    for prefix in AA9A_PATTERN_STARTS_WITH:
        if formatted_zipcode.startswith(prefix):
            return ' '.join([formatted_zipcode[:4], formatted_zipcode[-3:]])

    # Format: A9A 9AA
    # Coverage: E1, N1, W1
    if formatted_zipcode[:2] in A9A_PATTERN_STARTS_WITH:
        return ' '.join([formatted_zipcode[:3], formatted_zipcode[-3:]])

    # Format: A9 9AA or A99 9AA
    # Coverage: B, E, G, L, M, N, S, W
    if formatted_zipcode[0] in A9_OR_A99_PATTERN_STARTS_WITH:
        if len(formatted_zipcode) == 5:
            return ' '.join([formatted_zipcode[:2], formatted_zipcode[-3:]])
        elif len(formatted_zipcode) == 6:
            return ' '.join([formatted_zipcode[:3], formatted_zipcode[-3:]])

    # Format: AA9 9AA or AA99 9AA
    # Coverage: All other postcodes
    if len(formatted_zipcode) == 6:
        return ' '.join([formatted_zipcode[:3], formatted_zipcode[-3:]])
    elif len(formatted_zipcode) == 7:
        return ' '.join([formatted_zipcode[:4], formatted_zipcode[-3:]])

    raise ValueError(f'Unable to format {zipcode}')
