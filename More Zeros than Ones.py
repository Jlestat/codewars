def more_zeros(s: str) -> list:
    res = []
    for i in s:
        ascii_code = ord(i)
        if bin(ascii_code)[2:].count('0') > bin(ascii_code)[2:].count('1') and i not in res:
            res.append(i)
    return res