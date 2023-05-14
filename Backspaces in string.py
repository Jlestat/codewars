def clean_string(s: str) -> str:
    """

    :param s: str
    :return: str
    """
    final_str = ''
    for i, j in enumerate(s):
        if j == '#':
            final_str = final_str[:-1]
        else:
            final_str += j
    return final_str