
def string_breakers(n: int, st: str) -> str:
    """
    :param n: int
    :param st: str
    :return: str
    """
    final_str = st.replace(" ", "")
    return '\n'.join(final_str[i:i+n] for i in range(0, len(final_str), n))


print(string_breakers(32, 'gl 95fl5g 30t7vf4e3gd3j5ye phvalba1'))
