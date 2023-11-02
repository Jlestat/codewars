def no_odds(values: list) -> list:
    res = []
    for i in values:
        if i % 2 == 0:
            res.append(i)
    return res


print(no_odds([0, 1, 2, 3]))
