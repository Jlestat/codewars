def reverse_number(n: int) -> int:
    n = str(n)[::-1]
    try:
        return int(n)
    except:
        return -int(n[:-1])
