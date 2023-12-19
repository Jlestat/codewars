def solution(pairs: dict):
    res = ''
    for k, v in pairs.items():
        res += f'{k} = {v},'
    return res[:-1]


print(solution({'a': 1, 'b': 2}))