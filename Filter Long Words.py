def filter_long_words(sentence, n):
    curr_list = sentence.split()
    res = [i for i in curr_list if len(i) > n]
    return res