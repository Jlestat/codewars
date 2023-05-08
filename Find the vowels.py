def vowel_indices(word: str) -> list:
    "" "" 
    final_list = []
    for i in range(len(word)):
        if word[i] in 'aeiouyAEIOUY':
            final_list.append(i + 1)
        else:
            continue
    return final_list


print(vowel_indices('123456'))
