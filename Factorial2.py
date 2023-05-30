import math
def factorial(n: int) -> int:
    """
    :param n: int
    :return: int
    """
    if 0 <= n <= 12:
        return math.factorial(n)
    else:
        raise ValueError
