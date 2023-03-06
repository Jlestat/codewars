def find_nb(m):
    fin_sum = 0
    n = 0
    for i in str(m):
        fin_sum += pow((int(i) - n), 3)
        n += 1
    return fin_sum

print(find_nb(1071225))