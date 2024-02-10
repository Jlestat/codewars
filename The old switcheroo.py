def vowel_2_index(string):
    res = ''
    for i in range(len(string)):
        if string[i] in 'aeiou':
            res += str(i + 1)
        else:
            res += string[i]
    return res


print(vowel_2_index("this is my string"))
