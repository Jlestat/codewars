def name_value(my_list: list[str]) -> list[int]:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    n = 0
    result = []
    for i in my_list:
        curr_sum = 0
        for j in i:
            if j == ' ':
                continue
            else:
                curr_sum += alpha.index(j) + 1
        result.append(curr_sum * (n + 1))
        n += 1
    return result


print(name_value(["abc abc","abc abc","abc","abc"]))