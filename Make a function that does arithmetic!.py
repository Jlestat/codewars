def arithmetic(a: int, b: int, operator: str) -> int or float:
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'divide':
        return a / b
    else:
        return a * b
