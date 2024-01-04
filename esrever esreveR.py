def esrever(st: str) -> str:
    """
    :param st: str
    :return: str
    """
    try:
        curr_str = st[:-1]
        return curr_str[::-1] + st[-1]
    except:
        return ''