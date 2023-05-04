def sum_cubes(n: int) -> int:
    fin_sum = 0
    for i in range(1, n + 1):
        fin_sum += i ** 3
    return fin_sum