def to_weird_case(words: str) -> str:
    final_string = ''
    lst_str = [i for i in words.split()]
    for i in lst_str:
        curr_str = ''
        for j in range(len(i)):
            if j % 2 != 0:
                curr_str += i[j].lower()
            else:
                curr_str += i[j].upper()
        final_string += curr_str + ' '
    return final_string[:-1]




