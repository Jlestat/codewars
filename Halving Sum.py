def halving_sum(n: int) -> int:
    res = 0
    while n > 0:
        res += n
        n = n // 2
    return res


print(halving_sum(25))