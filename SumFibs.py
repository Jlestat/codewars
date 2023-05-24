def sum_fibs(n: int) -> int:
    final_sum = 0
    a = 1
    b = 1
    for i in range(n):
        if a % 2 == 0:
            final_sum += a
        a, b = b, a + b
    return final_sum


print(sum_fibs(9))