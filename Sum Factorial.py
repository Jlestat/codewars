def sum_factorial(lst):
    fin_sum = 0
    for i in lst:
        curr_fact = 1
        for j in range(1, i + 1):
            curr_fact *= j
        fin_sum += curr_fact
    return fin_sum
