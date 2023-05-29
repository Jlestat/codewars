def josephus(items: list, k: int) -> list:
    """
    :param items: list
    :param k: int
    :return: list
    """
    curr_list = items
    final_list = []
    i = 0
    while len(curr_list) > 0:
        j = (i + k - 1) % len(curr_list)
        final_list.append(curr_list[j])
        del curr_list[j]
        i = j if j < len(curr_list) else 0
    return final_list


print(josephus([1,2,3,4,5,6,7,8,9,10],2))