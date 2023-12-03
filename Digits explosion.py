def explode(s: str) -> str:
    res = ''
    for i in s:
        res += i * int(i)
    return res


print(explode('312'))