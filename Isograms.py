def is_isogram(string: str) -> bool:
    if len(string.lower()) == len(set(string.lower())):
        return True
    else:
        return False


