def has_unique_chars(string: str) -> bool:
    new_list = [i for i in string]
    if len(new_list) == len(set(new_list)):
        return True
    else:
        return False