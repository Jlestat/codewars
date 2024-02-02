def group(arr: list) -> list:
    result = []
    curr_list = []
    for i in arr:
        if i not in curr_list:
            curr_list.append(i)
    for i in curr_list:
        result.append([i] * arr.count(i))
    return result


print(group([3, 2, 6, 2, 1, 3]))