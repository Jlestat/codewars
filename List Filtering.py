def filter_list(l: list) -> list:
    final_list = [i for i in l if type(i) == int]
    return final_list


