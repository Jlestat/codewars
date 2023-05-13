def first_dup(s: str) -> str:
    """
    :param s: str
    :return: str
    """
    break_out_flag = False
    final_str = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                final_str += s[i]
                break_out_flag =True
                break
        if break_out_flag:
            break
    if final_str:
        return final_str
    else:
        return None


print(first_dup('1a2b3a3c'))