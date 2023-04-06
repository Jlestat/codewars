def remove_duplicate_words(s: str) -> str:
    cur_list = s.split()
    final_list = []
    for i in cur_list:
        if i in final_list:
            continue
        else:
            final_list.append(i)
    final_str = ' '.join(final_list)
    return final_str


print(remove_duplicate_words("my cat is my cat fat"))