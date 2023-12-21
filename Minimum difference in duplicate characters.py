def min_distance_repeating_char(s: str) -> tuple or None:
    """
    :param s: str, make a string.
    :return: tuple or None
    """
    if not s:
        return None
    char_indices = {}
    min_distance = float('inf')
    repeating_char = None
    for i, j in enumerate(s):
        if j in char_indices:
            distance = i - char_indices[j]
            if distance < min_distance:
                min_distance = distance
                repeating_char = j
        char_indices[j] = i
    return (min_distance, repeating_char) if repeating_char else None


print(min_distance_repeating_char("abka"))