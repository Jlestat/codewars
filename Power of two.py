def power_of_two(x: int) -> int:
    """

    :param x: int
    :return: int
    """
    for i in range(21):
        if 2 ** i == x:
            return True
    else:
        return False
