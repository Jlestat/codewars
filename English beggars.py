def beggars(values: list, n: int) -> list:
    fin_list = []
    for i in range(n):
        ind = list(range(i,len(values), n))
        curr_sum = 0
        for j in ind:
            curr_sum += values[j]
        fin_list.append(curr_sum)
    return fin_list