import math
def factorial(n: int) -> int:
    if 0 <= n <= 12:
        return math.factorial(n)
    else:
        raise ValueError
