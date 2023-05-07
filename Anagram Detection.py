# write the function is_anagram
def is_anagram(test, original):
    if set(test.lower()) == set(original.lower()) and len(test) == len(original):
        return True
    else:
        return False
