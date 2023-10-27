def number(lines: list) -> list:
    res = []
    for i, e in enumerate(lines):
        res.append(f'{i + 1}: {e}')
    return res


print(number(["a", "b", "c"]))