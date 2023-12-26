
def remove(s):
    words = s.split(' ')
    new_words = [word.rstrip('!') for word in words]
    return ' '.join(new_words)