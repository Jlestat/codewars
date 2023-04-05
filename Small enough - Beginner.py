def small_enough(array: list, limit: int) -> bool:
    if max(array) <= limit:
        return True
    else:
        return False