def solution(s):
    res_string = ''
    for i in s:
        if i == i.lower():
            res_string += i
        else:
            res_string += ' ' + i
    return res_string



print(solution('asdasdCdasda'))