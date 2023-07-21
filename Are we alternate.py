def is_alt(s: str) -> bool:
    """
    :param s: str
    :return: bool
    """
    vowels = 'aeiou'
    alph = 'bcdfghjklmnpqrstvwxyz'
    for i, j in zip(s, s[1:]):
        if i in vowels and j in vowels:
            return False
        if i in alph and j in alph:
            return False
    return True