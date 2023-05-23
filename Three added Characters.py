def added_char(s1: str, s2: str) -> str:
    """
    :param s1: str
    :param s2: str
    :return: str
    """
    for i in s2:
        if s2.count(i) > s1.count(i):
            return i


print(added_char("hello","checlclo"))