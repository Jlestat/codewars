def accum(s: str) -> str:
    final_str = ''
    d = 1
    for i in range(len(s)):
        curr_str = s[i] * d + '-'
        final_str += curr_str.title()
        d += 1

    return final_str[:-1]


