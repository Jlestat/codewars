def encrypt_this(text: str) -> str:
    list_of_str = text.split()
    final_list = []
    for i in range(len(list_of_str)):
        if len(list_of_str[i]) <= 1:
            final_list.append(str(ord(list_of_str[i])))
        elif len(list_of_str[i]) == 2:
            final_list.append(
                str(ord(list_of_str[i][0])) + list_of_str[i][-1])
        else:
            final_list.append(str(ord(list_of_str[i][0])) + list_of_str[i][-1] + list_of_str[i][2:-1] + list_of_str[i][1])

    return ' '.join(final_list).rstrip()


print(encrypt_this('A wise old owl lived in an oak'))