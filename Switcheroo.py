def switcheroo(s):
    res = ''
    for i in s:
        if i == 'b':
            res += 'a'
        elif i == 'a':
            res += 'b'
        else:
            res += i
    return res

