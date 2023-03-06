def is_prime(num: int) -> bool:
    if num == 1 or num == 0 or num < 0:
        return False
    else:
        if num % 2 == 0:
            return num == 2
        d = 3
        while d * d <= num and num % d != 0:
            d += 2
        return d * d > num


print(is_prime(73))