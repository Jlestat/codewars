def even_numbers(arr: list,n: int) -> list:
    final_list = []
    arr.reverse()
    for i in arr:
        if i % 2 == 0 and len(final_list) < n:
            final_list.append(i)
    final_list.reverse()
    return final_list


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))