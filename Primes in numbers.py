def primeFactors(n: int) -> str:
    """

    :param n: int
    :return: str
    """
    i = 2
    final_set = {}
    while n / i != 1:
        if n % i == 0:
            if i in final_set:
                final_set[i] = final_set[i] + 1
            else:
                final_set[i] = 1
            n = n / i
        else:
            i += 1

    if i in final_set:
        final_set[i] = final_set[i] + 1
    else:
        final_set[i] = 1
    final_str = ''
    res = sorted(final_set.items(), key=lambda a: a[0])

    for i in res:
        if i[1] == 1:
            final_str = final_str + '(' + str(i[0]) + ')'
        else:
            final_str = final_str + '(' + str(i[0]) + '**' + str(i[1]) + ')'
    return final_str
