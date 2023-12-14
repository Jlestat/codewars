def solve(strings : list[str]) -> list[int]:
    """
    :param strings: list[str]
    :return: list[int]
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for i in strings:
        i = i.lower()
        temp = 0
        for j in range(len(i)):

            if alpha.index(i[j]) == j:
                temp += 1
        res.append(temp)
    return res


print(solve(["abode","ABc","xyzD"]))