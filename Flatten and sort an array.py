def flatten_and_sort(array: list) -> list:
    final_list = []
    for i in range(len(array)):
        for j in array[i]:
            final_list.append(j)
    final_list.sort()
    return final_list


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))