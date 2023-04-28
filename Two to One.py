def longest(a1: str, a2: str) -> str:
    fin_str = list(set(a1 + a2))
    fin_str.sort()
    return ''.join(fin_str)


print(longest("aretheyhere", "yestheyarehere"))