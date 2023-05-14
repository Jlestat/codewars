def solution(s):
    """

    :param s: str
    :return: str
    """
    res_string = ''
    for i in s:
        if i == i.lower():
            res_string += i
        else:
            res_string += ' ' + i
    return res_string



print(solution('asdasdCdasda'))