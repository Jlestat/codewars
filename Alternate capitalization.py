def capitalize(s: str) -> list:
    "" "" 
    final_list = []
    first_str = ''
    second_str = ''
    for i in range(len(s)):
        if i % 2 != 0:
            first_str += s[i].upper()
        else:
            first_str += s[i]
    for i in range(len(s)):
        if i % 2 == 0:
            second_str += s[i].upper()
        else:
            second_str += s[i]
    final_list.append(second_str)
    final_list.append(first_str)
    return final_list


print(capitalize('abcdef'))
