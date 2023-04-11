def matrix_addition(a: list, b: list) -> list:
    return [[i + j for i, j in zip(first_el, second_el)] for first_el, second_el in zip(a,b)]


print(matrix_addition([1, 2], [1, 2, 3]))