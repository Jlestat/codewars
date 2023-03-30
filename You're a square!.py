import math
def is_square(n: int) -> bool:
    if n < 0:
        return False
    else:
        if math.sqrt(n) % 1 == 0:
            return True
        else:
            return False


print(is_square(0))