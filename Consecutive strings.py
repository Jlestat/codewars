def longest_consec(strarr: list, k: int) -> str:
    """
    """
    if k == 0 or k > len(strarr) or k < 0:
        return ''
    else:
        lst = [''.join(strarr[i:i + k]) for i in range(len(strarr))]
        return max(lst, key=lambda x: len(x))

