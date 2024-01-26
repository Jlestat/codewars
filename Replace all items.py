def replace_all(obj: list or str, find, rep):
    if type(obj) == list:
        res = []
        for i in obj:
            if i == find:
                res.append(rep)
            else:
                res.append(i)
        return res
    else:
        res = obj.replace(find, rep)
        return res


print(replace_all([1, 2, 3], 1, 2))