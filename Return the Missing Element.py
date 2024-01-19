def get_missing_element(seq: list) -> int:
    for i in range(10):
        if i not in seq:
            return i