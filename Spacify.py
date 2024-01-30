def spacify(string):
    a = ''
    for i in string:
        a += i + ' '
    try:
        if a[-1] == ' ' and a[-2] != ' ':
            a = a.rstrip()
            return a
        else:
            return a[:-1]
    except Exception:
        return ''