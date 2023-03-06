def alphabet_position(text):
    final_str = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in text.lower():
        if i in alpha:
            final_str += str(alpha.index(i) + 1) + ' '

    return final_str[:-1]


print(alphabet_position("The narwhal bacons at midnight."))