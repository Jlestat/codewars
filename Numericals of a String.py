def numericals(s: str) -> str:
    final_str = ''
    curr_str = ''
    for i in s:
        curr_str += i
        final_str += str(curr_str.count(i))
    return final_str


print(numericals('aaaaaaaaaaaa'))