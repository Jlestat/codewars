def basic_op(operator: str, value1: int, value2: int) -> int:
    return eval(f'{value1}{operator}{value2}')


print(basic_op('+', 4, 7))