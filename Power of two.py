def power_of_two(x: int) -> int:
    for i in range(21):
        if 2 ** i == x:
            return True
    else:
        return False
