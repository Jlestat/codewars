def reverse_alternate(s: str) -> str:
    list_of_strings = s.split()
    final_str = ''
    for i in range(len(list_of_strings)):
        if i % 2 != 0:
            final_str += list_of_strings[i][::-1] + ' '
        else:
            final_str += list_of_strings[i] + ' '
    return final_str[:-1]



print(reverse_alternate("Did it work?"))