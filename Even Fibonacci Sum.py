def even_fib(m: int) -> int:
    """
    :param m: int
    :return: int
    """
    final_sum = 0
    a = 0
    b = 1
    while a < m:
        if a % 2 == 0:
            final_sum += a
        a, b = b, a + b
    return final_sum


print(even_fib(10))