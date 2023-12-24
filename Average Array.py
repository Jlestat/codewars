def avg_array(arrays):
    num_arrays = len(arrays)
    array_length = len(arrays[0])
    averages = []
    for i in range(array_length):
        sum_at_index = sum(array[i] for array in arrays)
        averages.append(sum_at_index / num_arrays)

    return averages




print(avg_array([[1, 2, 3, 4], [5, 6, 7, 8]]))