def sum_dig_pow(a: int, b: int) -> list:
    final_list = []
    for num in range(a, b + 1):
        summed = sum(int(d) ** (idx + 1) for idx, d in enumerate(str(num)))
        if summed == num:
            final_list.append(num)
    return final_list


