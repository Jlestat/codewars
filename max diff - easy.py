def max_diff(lst: list) -> int:
    if lst:
        return max(lst) - min(lst)
    else:
        return 0