def find_even_index(arr: list) -> int:
    for i in range(0, len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i + 1:])
        if left == right:
            return i
    return -1
