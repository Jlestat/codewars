def generate_range(start, stop, step):
    res = []
    for i in range(start, stop + 1, step):
        res.append(i)
    return res