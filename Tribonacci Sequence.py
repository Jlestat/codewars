def tribonacci(signature: list, n: int) -> list:
    if n == 0:
        return []
    elif n < 3:
        return [signature[i] for i in range(0, n)]
    final_list = signature[:]
    for i in range(3, n):
        final_list.append(final_list[i-1] + final_list[i-2] + final_list[i-3])
    return final_list