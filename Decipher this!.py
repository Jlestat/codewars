def decipher_this(s: str) -> str:
    curr_list = s.split()
    final_list = []
    for i in curr_list:
        first_part_str = ''
        second_part_str = ''
        for j in i:
            if j.isdigit():
                first_part_str += j
            else:
                second_part_str += j
        try:
            if len(second_part_str) == 1:
                final_list.append(
                    str(chr(int(first_part_str))) + second_part_str[-1])
            else:
                final_list.append(str(chr(int(first_part_str))) + second_part_str[-1] + second_part_str[1:-1] + second_part_str[0])
        except:
            final_list.append(str(chr(int(first_part_str))) + second_part_str)
    return ' '.join(final_list)



print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))

