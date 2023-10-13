def get_sum(a: int,b: int) -> int:
    """

    :param a:
    :param b:
    :return:
    """
    fin_sum = 0
    if a < b:
        for i in range(a, b + 1):
            fin_sum += i
    else:
        for i in range(b, a + 1):
            fin_sum += i

    return fin_sum


print(get_sum(0, -1))