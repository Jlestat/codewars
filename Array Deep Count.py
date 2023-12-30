from functools import reduce


def deep_count(a: list) -> int:
    """

    :param a:
    :return:
    """
    if not isinstance(a, list):
        return 0
    if len(a) == 0:
        return 0
    return len(a) + reduce(lambda i, j : i + deep_count(j), a, 0)