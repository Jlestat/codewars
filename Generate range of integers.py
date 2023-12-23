def generate_range(start, stop, step):
    """

    :param start:
    :param stop:
    :param step:
    :return:
    """
    res = []
    for i in range(start, stop + 1, step):
        res.append(i)
    return res