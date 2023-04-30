def stray(arr: list) -> int:
    """

    :param arr: list
    :return: int
    """
    for i in arr:
        if arr.count(i) == 1:
            return i