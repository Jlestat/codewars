def sel_reverse(arr: list,l: int) -> list:
    """
    :param arr: list
    :param l: int
    :return: list
    """
    final_list = []
    if l == 0:
        return arr
    else:
        for i in range(0, len(arr), l):
            new_list = arr[i: i + l][::-1]
            for j in new_list:
                final_list.append(j)


        return final_list


print(sel_reverse([2,4,6,8,10,12,14,16], 3))
