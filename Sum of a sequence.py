def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    final_sum = 0
    for i in range(begin_number, end_number + 1, step):
        final_sum += i

    return final_sum


