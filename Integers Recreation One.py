import math

def list_squared(m: int, n: int) -> list:
    """
    :param m: int
    :param n: int
    :return: list
    """
    res = []
    for j in range(m, n + 1):
        div = set()
        for i in range(1, int(math.sqrt(j)+1)):
            if j % i == 0:
                div.add(i**2)
                div.add(int(j/i)**2)
        curr = sum(div)
        sr = math.sqrt(curr)
        if sr - math.floor(sr) == 0:
            res.append([j, curr])
    return res


print(list_squared(1, 250))