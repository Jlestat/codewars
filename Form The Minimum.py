def min_value(digits: list) -> int:
    set_dig = set(digits)
    new_list = list(set_dig)
    new_list.sort()
    return int(''.join([str(i) for i in new_list]))


print(min_value([1, 3, 1]))