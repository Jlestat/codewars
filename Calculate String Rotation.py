def shifted_diff(str1: str, str2: str):
    if len(str1) != len(str2):
        return -1

    for i in range(len(str1)):
        if str1 == str2:
            return i
        str2 = str2[1:] + str2[0]

    return -1
