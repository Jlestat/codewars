def solve(s: str) -> str:
    up = 0
    low = 0
    for i in s:
        if i == i.lower():
            low += 1
        else:
            up += 1
    if low >= up:
        return s.lower()
    else:
        return s.upper()