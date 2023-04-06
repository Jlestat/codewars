list_of_vowels = ['a', 'e', 'i', 'o', 'u']

def encode(st: str) -> str:
    final_str = ''
    for i in st:
        if i in list_of_vowels:
            final_str += str(list_of_vowels.index(i) + 1)
        else:
            final_str += i
    return final_str

def decode(st: str) -> str:
    final_str = ''
    for i in st:
        if i in '12345':
            final_str += str(list_of_vowels[int(i) - 1])
        else:
            final_str += i
    return final_str


print(encode('hello'))
print(decode('h2ll4'))