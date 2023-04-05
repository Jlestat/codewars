def capitals(word: str) -> list:
    final_list = []
    for i in range(len(word)):
        if word[i] == word[i].upper():
            final_list.append(i)
    return final_list


print(capitals('CodEWaRs'))