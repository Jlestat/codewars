def pairs(arr):
    res = 0
    for i in range(0, len(arr) - 1, 2):
        if abs(arr[i] - arr[i + 1]) == 1:
            res += 1
    return res


print(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]))