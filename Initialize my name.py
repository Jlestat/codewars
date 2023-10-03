def initialize_names(name):
    curr_list = name.split()
    if len(curr_list) <= 2:
        return name
    final_str = ''
    for i in range(len(curr_list)):
        if i == 0 or i == len(curr_list) - 1:
            final_str += curr_list[i] + ' '
        else:
            final_str += curr_list[i][0] + '. '
    return final_str[:-1]
