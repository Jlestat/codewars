def binary_array_to_number(arr: list) -> int:
    """
    :param arr: list
    :return: int
    """
    final_sum = 0
    n = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] != 0:
            final_sum += arr[i] * 2 ** n
        n += 1
    return final_sum


print(binary_array_to_number([1,1,1,1]))
