

def hex_string_to_RGB(hex_string):
    hex_string = hex_string.lstrip('#')
    curr_tuple = tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))
    res = {'r': curr_tuple[0],
           'g': curr_tuple[1],
           'b': curr_tuple[2]}
    return res


print(hex_string_to_RGB("#FF9933"))