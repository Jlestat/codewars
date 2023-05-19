def fib(n: int) -> int:
    a = 0
    b = 1
    final_list = []
    for i in range(n):
        final_list.append(a)
        a, b = b, a + b
    return final_list[n - 1]


print(fib(3))