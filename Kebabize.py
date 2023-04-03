def kebabize(st: str) -> str:
    final_str = ''
    for i in st:
        if i.isdigit():
            continue
        elif i == i.upper():
            final_str += '-' + i.lower()
        else:
            final_str += i
    try:
        if final_str[0] == '-':
            return final_str[1:]
        else:
            return final_str
    except:
        return final_str


print(kebabize('42'))
