def reverse_vowels(s: str) -> str:
    curr_list = []
    fin_str = ''
    for i in s[::-1]:
        if i in 'aeiouAEIOU':
            curr_list.append(i)
    for i in s:
        if i in 'aeiouAEIOU':
            fin_str += curr_list[0]
            curr_list.pop(0)
        else:
            fin_str += i
    return fin_str


print(reverse_vowels('Reverse Vowels In A String'))