def friend(x: list) -> list:
    final_list = []
    for i in x:
        if len(i) == 4:
            final_list.append(i)
    return final_list


