def filter_string(st: str) -> int:
    res = ''
    for i in st:
        if i.isdigit():
            res += i
    return int(res)