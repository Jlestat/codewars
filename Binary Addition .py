def add_binary(a: int,b: int) -> str:
    new_number = a + b
    final_str = ''
    while new_number > 0:
        final_str += str(new_number % 2)
        new_number //= 2
    return final_str[::-1]


print(add_binary(51, 12))
