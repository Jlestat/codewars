def reverse_middle(lst: list) -> list[int]:
    """
    :param lst: list
    :return: list
    """
    if len(lst) % 2 == 0:
        return lst[len(lst) // 2 - 1:len(lst) // 2 + 1][::-1]
    else:
        return lst[len(lst) // 2 - 1:len(lst) // 2 + 2][::-1]


print(reverse_middle([4, 3, 100, 1, 10]))