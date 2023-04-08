def reverse_letter(string: str) -> str:
    final_str = ''
    for i in string[::-1]:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            final_str += i
    return final_str
