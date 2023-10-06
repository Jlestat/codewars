def count_red_beads(n: int) -> int:
    """
    :param n: count of blue beads
    :return: count of red beads
    """
    if n < 2:
        return 0
    else:
        return n * 2 - 2