def in_array(array1: list, array2: list) -> list:
    final_list = []
    for i in array1:
        for j in array2:
            if i in j:
                if i in final_list:
                    continue
                else:
                    final_list.append(i)
    final_list.sort()
    return final_list


