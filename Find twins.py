def elimination(arr: list) -> int:
    """
    :param arr: list
    :return: int
    """
    for i in arr:
        if arr.count(i) == 2:
            return i