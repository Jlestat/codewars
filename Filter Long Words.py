def filter_long_words(sentence: list, n: int) -> list:
    curr_list = sentence.split()
    res = [i for i in curr_list if len(i) > n]
    return res