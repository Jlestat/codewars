def expanded_form(num: int) -> str:
    final_string = ''
    start = 0
    for i in str(num):
        if i != '0':
            final_string += i + '0' * (len(str(num)) - 1 - start) + ' + '
        start += 1
    return final_string[:-3]



