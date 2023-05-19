def fib(n: int) -> int:
    """
    :param n: int
    :return: int
    """
    a = 0
    b = 1
    final_list = []
    for i in range(n):
        final_list.append(a)
        a, b = b, a + b
    return final_list[n - 1]


print(fib(3))