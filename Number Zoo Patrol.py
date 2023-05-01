def find_missing_number(numbers: list) -> int:
    orig_list = [i for i in range(1, max(numbers) + 1)]
    for i in orig_list:
        if i not in numbers:
            return i


print(find_missing_number([2, 3, 4]))