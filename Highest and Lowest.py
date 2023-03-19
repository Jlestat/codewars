def high_and_low(numbers: str) -> str:
    list_of_numbers = [int(i) for i in numbers.split()]
    return f'{max(list_of_numbers)} {min(list_of_numbers)}'


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
