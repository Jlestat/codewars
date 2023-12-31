def find_missing_numbers(arr):
    try:
        r = [i for i in range(arr[0], arr[-1])]
    except Exception:
        return []
    result = []
    for i in r:
        if i not in arr:
            result.append(i)
    return result


print(find_missing_numbers([]))