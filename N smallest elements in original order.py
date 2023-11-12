def first_n_smallest(arr, n):
    if n <= 0:
        return []
    enumerated_arr = list(enumerate(arr))
    sorted_arr = sorted(enumerated_arr, key=lambda x: (x[1], x[0]))
    result = sorted(sorted_arr[:n], key=lambda x: x[0])
    return [x[1] for x in result]


print(first_n_smallest([0, -5, -3, 10, -4, -3, -5, 4, 4, 10, 4, 1, 0, 1, 0, 6, 2, -6, 0, -8, -4, 10, 7, 4, -6, 4, -2], 6))