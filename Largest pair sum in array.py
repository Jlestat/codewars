def largest_pair_sum(numbers: list) -> int:
    res = 0
    res += max(numbers)
    numbers.remove(max(numbers))
    res += max(numbers)
    return res


print(largest_pair_sum([10,14,2,23,19]))