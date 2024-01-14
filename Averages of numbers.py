def averages(arr: list) -> list:
    """
    :param arr: list
    :return: list
    """
    try:
        res = []
        for i in range(len(arr) - 1):

            if i == len(arr):
                res.append(arr[i] / 2)
            else:
                res.append((arr[i] + arr[i + 1]) / 2)

        return res
    except Exception:
        return []


print(averages([1, 3, 5, 1, -10]))