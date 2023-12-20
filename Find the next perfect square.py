import math
def find_next_square(sq: int) -> int:
    """
    :param sq: int
    :return: int
    """
    if str(math.sqrt(sq))[-1] == '0':
        return int(math.sqrt(sq) + 1) ** 2
    else:
        return -1


print(find_next_square(121))
