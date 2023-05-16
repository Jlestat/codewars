def fibonacci(n: int) -> list:
    """
    :param n: int
    :return: list
    """
    final_list = []
    a = 0
    b = 1
    for i in range(n):
        final_list.append(a)
        a, b = b, a + b
    return final_list


print(fibonacci(-4))