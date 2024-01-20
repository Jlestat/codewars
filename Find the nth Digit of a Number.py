def find_digit(num: int, nth: int) -> int:
    if nth <= 0:
        return -1
    else:
        try:
            if str(num)[::-1][nth - 1].isdigit():
                return int(str(num)[::-1][nth - 1])
            else:
                return 0
        except Exception:
            return 0

print(find_digit(-456, 4))