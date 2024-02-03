def fibonacci(n: int) -> int:
    a = 0
    b = 1
    result = []
    for i in range(n + 1):
        result.append(a)
        a, b = b, a + b
    return result[n]


print(fibonacci(34))