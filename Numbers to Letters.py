def switcher(arr: list) -> str:
    alpha = 'zyxwvutsrqponmlkjihgfedcba!? '
    res = ''
    for i in arr:
        res += alpha[int(i) - 1]
    return res


print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))