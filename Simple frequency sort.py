def solve(arr):
    n = set(arr)
    f = {}
    for i in n:
        if arr.count(i) in f:
            f[arr.count(i)].append(i)
        else:
            f[arr.count(i)] = [i]
    res = []
    for count in sorted(f.keys(), reverse=True):
        for i in sorted(f[count]):
            res.extend([i for y in range(count)])
    return res


print(solve([2,3,5,3,7,9,5,3,7]))
