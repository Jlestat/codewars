def pyramid(n: int) -> list:
    return [[1] * i for i in range(1, n + 1)]


print(pyramid(0))
