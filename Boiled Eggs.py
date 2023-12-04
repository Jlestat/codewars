import math


def cooking_time(eggs: int) -> int:
    """
    :param eggs: int
    :return: int
    """
    return math.ceil(eggs / 8) * 5


print(cooking_time(5))
