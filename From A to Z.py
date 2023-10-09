def gimme_the_letters(sp: str) -> str:
    """
    :param sp: str
    :return: str
    """
    alph = 'abcdefghijklmnopqrstuvwxyz'
    if sp[0] == sp[0].upper():
        return alph[alph.index(sp[0].lower()):alph.index(sp[-1].lower()) + 1].upper()
    else:
        return alph[alph.index(sp[0].lower()):alph.index(sp[-1].lower()) + 1]


print(gimme_the_letters("Q-Z"))