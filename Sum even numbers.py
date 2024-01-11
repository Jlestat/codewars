def sum_even_numbers(seq):
    res = 0
    for i in seq:
        if i % 2 == 0:
            res += i
    return res