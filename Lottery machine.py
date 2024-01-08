def lottery(s: str):
    curr_list = []
    for i in s:
        if i.isdigit() and i not in curr_list:
            curr_list.append(i)
    if len(curr_list) == 0:
        return 'One more run!'
    else:
        return ''.join(curr_list)
