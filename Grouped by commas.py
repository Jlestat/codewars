def group_by_commas(n: int) -> str:
    """

    :param n: int
    :return: str
    """
    final_str = ''
    n = str(n)[::-1]
    for i in range(len(str(n))- 1, -1, -1):
        if i % 3 == 0:
            final_str += str(n)[i] + ','
        else:
            final_str += str(n)[i]
    return final_str[:-1]


print(group_by_commas(35235235))