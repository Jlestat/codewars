def spacey(array):
    final_list = []
    for i in range(1, len(array) + 1):
        curr_str = ''
        for j in range(i):
            curr_str += array[j]
        final_list.append(curr_str)
    return final_list
    
    
