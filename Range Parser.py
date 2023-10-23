import re


def range_parser(s: str) -> list:
    res = []
    new_list = re.split(",|, ", s)
    for i in new_list:
        new_i = i.strip()
        if '-' in new_i and ':' in new_i:
            for j in range(int(new_i[:new_i.index('-')]), int(new_i[new_i.index('-') + 1:new_i.index(':')] ) + 1,
                           int(new_i[new_i.index(':') + 1:])):
                res.append(j)
        elif '-' in new_i:
            for j in range(int(new_i[:new_i.index('-')]), int(new_i[new_i.index('-') + 1:]) + 1):
                res.append(j)
        else:
            res.append(int(i))
    return res


print(range_parser("1-10,14, 20-25:2"))
