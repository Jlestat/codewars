def elimination(arr: list):
    for i in arr:
        if arr.count(i) == 2:
            return i