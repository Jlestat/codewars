def changer(s: str) -> str:
    alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    curr_str = ''
    final_str = ''
    for i in s.lower():
        if i.isdigit() or i == ' ':
            curr_str += i
        else:
            curr_str += alpha[alpha.index(i) + 1]
    for i in curr_str:
        if i in 'aeiou':
            final_str += i.upper()
        else:
            final_str += i.lower()
    return final_str


print(changer('Hello World'))