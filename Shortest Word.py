def find_short(s: str) -> int:
    curr_list = [i for i in s.split()]
    curr_min = len(curr_list[0])
    for i in curr_list:
        if len(i) < curr_min:
            curr_min = len(i)

    return curr_min


