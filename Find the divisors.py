def divisors(integer: int) -> list:
    final_list = []
    for i in range(2, integer):
        if integer % i == 0:
            final_list.append(i)
    if len(final_list) == 0:
        return f'{integer} is prime'
    else:
        return final_list