def sum_digits(number):
    fin_sum = 0
    for i in str(number):
        if i.isdigit():
            fin_sum += int(i)
    return fin_sum
