def cut_log(p: list, n: int) -> list:
    max1 = [0]
    for j in range(1, n + 1):
        com = -float("inf")
        for i in range(1, j + 1):
            com = max(p[i - 1 + 1] + max1[j - i], com)
        max1.append(com)
    return max1[-1]
