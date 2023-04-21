def two_sum(numbers: list, target: int) -> list:
    for i, j in enumerate(numbers):
        number = target - j
        if number in numbers and numbers.index(number) != i:
            return [i, numbers.index(target-j)]


print(two_sum([1, 1, 1, 1, 1, 1, 1234,5678,9012, 1, 1, 1, 2, 3], 14690))