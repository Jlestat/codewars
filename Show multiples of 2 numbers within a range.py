def multiples(s1: int, s2: int, s3: int) -> list:
    result = []
    for i in range(1, s3):
        if i % s1 == 0 and i % s2 == 0:
            result.append(i)
    return result


print(multiples(2, 4, 40))