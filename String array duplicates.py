def dup(arry: list) -> list:
    final_list = []
    for i in arry:
        out = ''
        for j in range(len(i) - 1):
            if i[j] != i[j + 1]: out += i[j]
        if i[-1] != out[-1]: out += i[-1]
        final_list.append(out)

    return final_list


print(dup(["abracadabra","allottee","assessee"]))