def stray(arr: list) -> int:
    for i in arr:
        if arr.count(i) == 1:
            return i