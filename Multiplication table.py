def multiplication_table(size):
    final_list = []
    for num in range(1, size + 1):
        final_list.append([num * size for size in range(1, size + 1)])
    return final_list



