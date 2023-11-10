def passed(lst: list) -> int or str:
    n = 0
    c = 0
    for i in lst:
        if i <= 18:
            n += i
            c += 1
    if c == 0:
        return 'No pass scores registered.'
    else:
        return round(n / c)

print(passed([16, 21, 18, 15, 20, 28, 28, 23, 28, 20, 26, 28, 27, 15, 25, 26, 21, 16, 20, 29, 18, 24, 30, 27, 29, 19, 27, 29, 28, 26, 18, 19, 27, 30, 22, 30, 20, 21, 25, 18, 17, 29, 19, 28, 25, 17, 15]))
