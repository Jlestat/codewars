import re
def solve(s: str) -> int:

    s = re.sub('[aeiou]+', ' ', s)
    s = s.split(' ')
    max_value = 0
    alpha = '-abcdefghijklmnopqrstuvwxyz'
    for i in s:
        t = 0
        for j in i:
            t += alpha.index(j)
            if t > max_value:
                max_value = t
    return max_value


print(solve('zodiac'))