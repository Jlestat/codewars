def multiple(x: int) -> str:
    """
    :param x: int
    :return: str
    """
    if x % 3 == 0 and x % 5 == 0:
        return 'BangBoom'
    elif x % 5 == 0:
        return 'Boom'
    elif x % 3 == 0:
        return 'Bang'
    else:
        return 'Miss'