import collections

def dominator(arr: list) -> int:
    """
    :param arr: list
    :return: int
    """
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return arr[0]
    else:
        n = collections.Counter(arr).most_common()
        print(n)
        if n[0][1] == n[1][1]:
            return -1
        else:
            if arr.count(n[0][0]) > len(arr) // 2:
                return n[0][0]
            else:
                return -1



print(dominator([1]))
