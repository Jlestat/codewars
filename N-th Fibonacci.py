def nth_fib(n: int) -> int:
    fib_list = []
    a = 0
    b = 1
    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list[-1]


print(nth_fib(4))