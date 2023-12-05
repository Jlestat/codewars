def average_string(s):
    digit = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    digit_str = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    res = 0
    list_of_str = s.split()
    for i in list_of_str:
        try:
            res += digit[i]
        except Exception:
            return 'n/a'
    if res == 0 and 'zero' in list_of_str:
        return 'zero'
    elif res == 0 and 'zero' not in list_of_str:
        return 'n/a'
    final_res = res // len(list_of_str)
    return digit_str[final_res]


print(average_string("123"))