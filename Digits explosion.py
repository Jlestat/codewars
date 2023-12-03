def explode(s: str) -> str:
    """
    :param s: str
    :return: str
    """
    res = ''
    for i in s:
        res += i * int(i)
    return res


print(explode('312'))